from django.db.models import QuerySet, Q
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from profiles.models import Profile
from .models import Question, Answer, QuestionnaireResult
import json
import random as rd
from django.core.exceptions import ObjectDoesNotExist


class Matching:
    PROFILES_FOR_JSON_MATCHING = 5
    PROFILES_FOR_PROFILE_MATCHING = 10

    @staticmethod
    def get_questionnaire_results(profile=None):
        all_profiles = Profile.objects.filter(~Q(questionnaire_result=None))
        if profile is not None:
            all_profiles = all_profiles.filter(~Q(pk=profile.pk))

        return [profile.questionnaire_result for profile in all_profiles]

    @staticmethod
    def matching_with_profile(profile):

        print(profile.to_json())
        try:
            if profile.questionnaire_result is None:
                return []
        except ObjectDoesNotExist:
            return []

        questionnaire_results = Matching.get_questionnaire_results(profile)

        matching_profiles = list(
            map(lambda x: Matching.calculate_similarity_with_profile(x, profile),
                questionnaire_results))

        matching_profiles = Matching.sanitize_similarity(matching_profiles, n=Matching.PROFILES_FOR_PROFILE_MATCHING)

        return Matching.generate_json_result(matching_profiles)

    @staticmethod
    def matching_with_json_answers(answers):
        questionnaire_results = Matching.get_questionnaire_results()

        matching_profiles = list(
            map(lambda x: Matching.calculate_similarity_with_json(x, answers),
                questionnaire_results))

        matching_profiles = Matching.sanitize_similarity(matching_profiles, n=Matching.PROFILES_FOR_JSON_MATCHING)

        return Matching.generate_json_result(matching_profiles)

    @staticmethod
    def calculate_similarity_with_json(questionnaire_result, answers):
        same_answers_count = 0
        for answer in answers:
            if isinstance(answer['result'], list):
                same_answers_count += questionnaire_result.answers.filter(pk__in=answer['result']).count()
            else:
                same_answers_count += questionnaire_result.answers.filter(pk=answer['result']).count()

        return questionnaire_result.profile.pk, same_answers_count

    @staticmethod
    def calculate_similarity_with_profile(questionnaire_result, profile):
        pks = profile.questionnaire_result.answers.values_list('pk', flat=True)
        same_answers_count = questionnaire_result.answers.filter(pk__in=pks).count()
        return questionnaire_result.profile.pk, same_answers_count

    @staticmethod
    def sanitize_similarity(matching_profiles, n):
        matching_profiles = sorted(matching_profiles,
                                   key=lambda x: x[1],
                                   reverse=True)

        max_value = max(map(lambda x: x[1], matching_profiles))
        matching_profiles = list(
            map(lambda x: (x[0], int((x[1] / max_value) * rd.randint(80, 91))),
                matching_profiles))
        return matching_profiles[:n]

    @staticmethod
    def generate_json_result(matching_profiles):
        profiles_ids, percentage_match = zip(*matching_profiles)

        profiles = Profile.objects.filter(pk__in=profiles_ids)
        json_profiles = list(map(lambda x: x.to_json(), profiles))

        for profile in json_profiles:
            profile['percentage_match'] = percentage_match[profiles_ids.index(profile['pk'])]

        json_profiles = sorted(json_profiles, key=lambda x: x['percentage_match'], reverse=True)
        return json_profiles
