from django.db import models
from profiles.models import Profile

class Conversation(models.Model):
    inquire = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                   related_name="started_conversations", null=True)
    mentor = models.ForeignKey(Profile, on_delete=models.SET_NULL,
                                  related_name="mentored_conversations", null=True)

    def to_json(self):
        return {
            "inquire": None if self. inquire is None else self.inquire.to_json(),
            "mentor": None if self.mentor is None else self.mentor.to_json(),
            "messages": [m.to_json() for m in self.messages.all()]
        }


class Message(models.Model):
    sender = models.OneToOneField(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True, blank=True)

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')

    def to_json(self):
        return {
            "sender": self.sender.pk,
            "text": self.text,
            "time": str(self.time)
        }