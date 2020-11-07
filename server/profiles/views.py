from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from .models import Profile, User
from questionnaire.models import QuestionnaireResult, Question
from django.views.decorators.csrf import csrf_exempt
import json
import faker
import random as rd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = request.user.profile

        response = dict(profile=profile.to_json(),
                        mentored_conversations=[
                            c.to_json() for c in profile.mentored_conversations.all()],
                        started_conversations=[
                            c.to_json() for c in profile.started_conversations.all()]
                        )
        return JsonResponse(response)

def scrape_profiles(request):
    fake = faker.Faker()

    all_questions = list(Question.objects.all())

    for i in range(15):
        profile = Profile()
        profile.gender = rd.choice([0,1])

        if profile.gender == 0:
            profile.first_name = fake.first_name_male()
            profile.picture_url = f"https://randomuser.me/api/portraits/men/{rd.randint(0, 56)}.jpg"
        else:
            profile.first_name = fake.first_name_female()
            profile.picture_url = f"https://randomuser.me/api/portraits/women/{rd.randint(0,87)}.jpg"

        profile.city = fake.city()
        profile.story = fake.text(max_nb_chars=1000)
        profile.matching_preference = 1
        profile.birthday_year = rd.randint(1990, 2008)
        profile.save()

        user = User(username=f"generated_{profile.pk}", password="test")
        profile.user = user

        user.save()

        questionnaire_result = QuestionnaireResult(profile=profile)
        questionnaire_result.save()
        n = 10
        n_questions = rd.sample(all_questions, n)
        answers = [pick_random_answer(list(question.answers.all())) for question in n_questions if question.style != 'slider']
        for answer in answers:
            questionnaire_result.answers.add(answer)

        questionnaire_result.save()
    return HttpResponse("Generated")


def pick_random_answer(answers):
    return rd.choice(answers)


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        profile_json = json.loads(request.body)
        profile = Profile(
            first_name=profile_json['first_name'],
            birthday_year=profile_json['birthday_year'],
            gender=profile_json['gender'],
            city=profile_json['city'],
            story=profile_json['story'],
            matching_preference=profile_json['matching_preference']
        )
        profile.save()

        return JsonResponse(dict(success=True, id=profile.pk))

    return HttpResponseNotFound()
