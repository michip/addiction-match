from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404, get_object_or_404
from profiles.models import Profile

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
@csrf_exempt
def next_question(request):
    return JsonResponse({"not_implemented":"yet..."})
