from django.db.models import QuerySet, Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Question, Answer
import json
from .matching import Matching


@csrf_exempt
def process_answers(request):
    if request.method == 'POST':
        answers = json.loads(request.body)
        profiles_list = Matching.matching_with_json_answers(answers)
        return JsonResponse(profiles_list, safe=False)
    return HttpResponseNotFound()


def with_percentage_match(profile, percentage_match):
    profile['percentage_match'] = percentage_match
    return profile


def calculate_next_question(last_question):
    parent_answer = last_question.follows_after_answer

    possible_questions = None

    if parent_answer is not None:
        possible_questions = parent_answer.followup_questions
        possible_questions = possible_questions.filter(order__gt=last_question.order)

        if not possible_questions.exists():
            possible_questions = calculate_next_question(parent_answer.question)
    else:
        possible_questions = Question.objects.filter(follows_after_answer=None, order__gt=last_question.order)

    if isinstance(possible_questions, QuerySet):
        possible_questions = possible_questions.order_by('order').first()

    return possible_questions


@csrf_exempt
def next_question(request):
    if request.method == 'POST':

        past_questions = json.loads(request.body)

        last_question_json = None
        new_question = None

        if past_questions:
            last_question_json = past_questions[-1]

        if last_question_json:
            last_question = get_object_or_404(Question, pk=last_question_json["question"])
            # Only allow followups on radio buttons
            if last_question.style == 'radio' and "result" in last_question_json:
                last_answer = get_object_or_404(Answer, pk=last_question_json["result"])
                if last_answer.followup_questions.exists():
                    new_question = last_answer.followup_questions.order_by('order').first()

            # In case we have an answer that does not imply a followup question
            if new_question is None or not new_question:
                new_question = calculate_next_question(last_question)
        else:
            # First question
            new_question = Question.objects.filter(follows_after_answer=None).order_by('order').first()

        if new_question is None or not new_question:
            [save_answer(question) for question in past_questions]
            return JsonResponse(dict(last_question=True))
        else:
            return JsonResponse(new_question.to_json())


def save_answer(question):
    answer = Answer(value=question['result'], question=Question.objects.get(pk=question['question']))
