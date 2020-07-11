from django.contrib import admin
from .models import User, StudentProfile, TeacherProfile

admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(User)