from django.contrib import admin
from .models import Task, Test, PinTest, Submission, Result, PinResult


class TaskAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'slug', 'enabled'


class TestAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'enabled'


class PinTestAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'enabled'


class SubmissionAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'author', 'compiled'
