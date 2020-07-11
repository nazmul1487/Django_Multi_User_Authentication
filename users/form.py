from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, StudentProfile, TeacherProfile
from django.db import transaction


class CreateStudentForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = StudentProfile.objects.create(user=user)
        student.save()
        return user


class CreateTeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = TeacherProfile.objects.create(user=user)
        teacher.save()
        return user
