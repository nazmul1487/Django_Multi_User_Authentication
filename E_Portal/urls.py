"""E_Portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from users.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',UserLoginView.as_view(), name='login'),
    path('dashboard/',HomeView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('student_register/', StudentRegisterView.as_view(), name='student_register'),
    path('teacher_register/', TeacherRegisterView.as_view(), name='teacher_register'),
    path('logout/', logoutUser, name='logout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name='password_reset'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name='password_reset_complete'),

    path('account/', accountSetting, name='account')
]




urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)