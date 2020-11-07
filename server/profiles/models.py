from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    MATCHING_PREFERENCES = [
        (0, 'no_match'),
        (1, 'mentor'),
    ]

    GENDERS = [
        (0, 'male'),
        (1, 'female'),
        (2, 'other'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                null=True, default=None)

    first_name = models.CharField(max_length=64)
    birthday_year = models.IntegerField(default=1990)
    gender = models.IntegerField(choices=GENDERS, default=0)

    picture_url = models.CharField(max_length=300, default=None, null=True)

    city = models.CharField(max_length=64, default=None, null=True)
    story = models.CharField(max_length=2000, default=None, null=True)

    matching_preference = models.IntegerField(choices=MATCHING_PREFERENCES, default=1)

    def to_json(self):
        # TODO: add picture
        return {
            "pk": self.pk,
            "first_name": self.first_name,
            "birthday_year": self.birthday_year,
            "gender": next((identifier for i, identifier in self.GENDERS if i == self.gender)),
            "matching_preference": next((identifier for i, identifier in self.MATCHING_PREFERENCES if i == self.matching_preference)),
            "picture_url": self.picture_url,
            "city": self.city,
            "story": self.story
        }

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
