from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.http import JsonResponse
from .models import Conversation, Message
from profiles.models import Profile
import json
from django.views.decorators.csrf import csrf_exempt
import faker


@csrf_exempt
def generate_message(request):
    fake = faker.Faker()
    if request.method == 'POST':
        requesting_message = json.loads(request.body)
        conversation = get_object_or_404(Conversation, pk=requesting_message['conversation'])
        sender = get_object_or_404(Profile, requesting_message['message_from'])
        text = fake.text(max_nb_chars=100)

        message = Message(sender=sender, text=text, conversation=conversation)
        message.save()

        return JsonResponse(dict(success=True, message=message.pk))

    return HttpResponseNotFound()

# TODO: Authentication
def get_conversation(request, id):
    conversation = get_object_or_404(Conversation, pk=id)
    return JsonResponse(conversation.to_json())


@csrf_exempt
def create_conversation(request):
    if request.method == 'POST':
        conversation_json = json.loads(request.body)

        temporary_profile = Profile(first_name=conversation_json['first_name'],
                                    picture_url="https://www.pngitem.com/pimgs/m/421-4212341_default-avatar-svg-hd-png-download.png")
        temporary_profile.save()

        inquire = temporary_profile
        mentor = get_object_or_404(Profile, pk=conversation_json['mentor'])

        conversation = Conversation(inquire=inquire, mentor=mentor)
        conversation.save()

        return JsonResponse(dict(success=True, id=conversation.pk))


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        message_json = json.loads(request.body)
        sender = get_object_or_404(Profile, pk=message_json['sender'])
        conversation = get_object_or_404(Conversation, pk=message_json['conversation'])
        message = Message(sender=sender, text=message_json['text'], converation=conversation)
        message.save()

        return JsonResponse(dict(success=True, id=message.pk, time=message.time))


def get_new_messages(request):
    last_message_json = json.loads(request.body)
    last_message = get_object_or_404(Message, pk=last_message_json['last_message'])

    conversation = last_message.conversation

    messages = conversation.messages.filter(time__gt=last_message.time).order_by('time')

    return JsonResponse([m.to_json() for m in messages])


