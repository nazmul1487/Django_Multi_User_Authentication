
from django.urls import path, include
from users.views import *
urlpatterns = [

    path('',HomeView.as_view(), name='home'),
]