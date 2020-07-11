from _ast import mod

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='s_profile')
    u_id = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    s_profile = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='t_profile')
    t_id = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    t_profile = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         if User.is_teacher:
#             TeacherProfile.objects.create(user=instance)
#
#         else:
#             StudentProfile.objects.create(user=instance)






# # save_user_profile_using_signal
# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.profile.save()