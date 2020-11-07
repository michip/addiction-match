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
from questionnaire.matching import Matching
from django.utils.crypto import get_random_string
from conversations.models import Conversation

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        profile = request.user.profile

        profiles = list(Profile.objects.all())

        #TODO: remove the mock up
        started_conversations = [
            Conversation(inquire=profile, mentor=rd.choice(profiles)) for _ in range(5)]

        mentored_conversations = [
            Conversation(inquire=rd.choice(profiles), mentor=profile) for _ in range(5)]

        response = dict(profile=profile.to_json(),
                        mentored_conversations=[
                            c.to_json() for c in mentored_conversations],
                        started_conversations=[
                            c.to_json() for c in started_conversations],
                        matches=Matching.matching_with_profile(profile)
                        )
        return JsonResponse(response)


def scrape_profiles(request):
    fake = faker.Faker()

    all_questions = list(Question.objects.all())

    for i in range(15):

        user = User(username=f"generated_{get_random_string(length=16)}")
        user.set_password("junctiontest")
        user.save()

        profile = user.profile
        profile.gender = rd.choice([0, 1])

        if profile.gender == 0:
            profile.first_name = fake.first_name_male()
            profile.picture_url = f"https://randomuser.me/api/portraits/men/{rd.randint(0, 56)}.jpg"
        else:
            profile.first_name = fake.first_name_female()
            profile.picture_url = f"https://randomuser.me/api/portraits/women/{rd.randint(0, 87)}.jpg"

        profile.city = fake.city()
        profile.story = fake.text(max_nb_chars=1000)
        profile.matching_preference = 1
        profile.birthday_year = rd.randint(1990, 2008)
        profile.save()

        profile.save()

        profile.questionnaire_result = QuestionnaireResult()
        profile.questionnaire_result.save()

        n = 10
        n_questions = rd.sample(all_questions, n)
        answers = [pick_random_answer(list(question.answers.all())) for question in n_questions if
                   question.style != 'slider']
        for answer in answers:
            profile.questionnaire_result.answers.add(answer)

        profile.questionnaire_result.save()

    return HttpResponse("Generated")


def pick_random_answer(answers):
    return rd.choice(answers)


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        profile_json = json.loads(request.body)

        user = User(username=profile_json['username'])
        user.set_password(profile_json['password'])
        user.save()

        profile = user.profile
        profile.first_name = profile_json['first_name'],
        profile.birthday_year = profile_json['birthday_year'],
        profile.gender = profile_json['gender'],
        profile.city = profile_json['city'],
        profile.story = profile_json['story'],
        profile.matching_preference = profile_json['matching_preference']
        profile.save()

        return JsonResponse(dict(success=True, id=profile.pk))

    return HttpResponseNotFound()
