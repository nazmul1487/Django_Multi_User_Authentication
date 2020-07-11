from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

from .form import CreateStudentForm, CreateTeacherForm
from .models import TeacherProfile, StudentProfile


class HomeView(TemplateView):
    template_name = 'dashboard.html'


class StudentRegisterView(CreateView):
    form_class = CreateStudentForm
    template_name = 'user/student_register.html'
    success_url = reverse_lazy('login')


class TeacherRegisterView(CreateView):
    form_class = CreateTeacherForm
    template_name = 'user/teacher_register.html'
    success_url = reverse_lazy('login')


class RegisterView(TemplateView):
    template_name = 'user/register.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('home')


def logoutUser(request):
    logout(request)
    return redirect('login')


def accountSetting(request):
    # queryset = []
    if request.user.is_student:
        queryset = StudentProfile.objects.filter(user=request.user).first()
    else:
        queryset = TeacherProfile.objects.filter(user=request.user).first()
    context = {'data': queryset}
    return render(request, 'user/account_setting.html',context)