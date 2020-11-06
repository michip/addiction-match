from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotFound
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
import json

def get_profile(request, id):
    profile = get_object_or_404(Profile, pk=id)
    return JsonResponse({
        "first_name": profile.first_name
    })

@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        profile_json = json.loads(request.body)
        profile = Profile(first_name=profile_json['first_name'])
        profile.save()

        return JsonResponse(dict(success=True, id=profile.pk))

    return HttpResponseNotFound()
