from django.contrib import admin
from . import models

# Register your models here.

from Zoom_App.models import Lesson
admin.site.register(Lesson)

class LessonAdmin(admin.ModelAdmin):
    pass