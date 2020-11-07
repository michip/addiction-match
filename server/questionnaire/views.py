from django.db.models import QuerySet
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from profiles.models import Profile
from .models import Question, Answer
import json

@csrf_exempt
def process_answers(request):
    if request.method == 'POST':
        # if we don't have more questions let's proceed with matchmaking...
        profiles_ids_with_matching_percentage = matchmake(request.body)
        profiles_list = get_profiles(profiles_ids_with_matching_percentage)
        return JsonResponse(profiles_list, safe=False)
    return HttpResponseNotFound()

def matchmake(results):
    # Matchmaking algorithm should go there
    return {1: 97, 2: 73, 3:68, 4: 65, 5: 17}

def get_profiles(profiles_ids_with_matching_percentage):
    profiles_ids = profiles_ids_with_matching_percentage.keys()
    profiles = Profile.objects.filter(pk__in=profiles_ids)
    get_percentage = lambda x: profiles_ids_with_matching_percentage.get(x)
    json_profiles = map(lambda x: x.to_json(), profiles)
    json_profiles_with_percentage_match = map(lambda x: with_percentage_match(x, get_percentage) ,json_profiles)
    return list(json_profiles_with_percentage_match)

def with_percentage_match(profile, get_percentage):
    profile['percentage_match'] = get_percentage(profile.get('pk'))
    return profile


# Input: previous questions and answers
# if last question: "last_question" : "true"

"""
[
    {
        "question": id
        "result": 10 /slider
        "result: 1 /radio
        "result": [1, 2, 3] /multiple
    },
    ...,
    {
        "question": id
        "result: {} #Answer
    }
]

"""

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
            return JsonResponse(dict(last_question=True))
        else:
            return JsonResponse(new_question.to_json())
