from django.contrib import admin
from .models import Task, Test, PinTest, Submission, Result, PinResult


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'slug', 'enabled'


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'enabled'


@admin.register(PinTest)
class PinTestAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'enabled'


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = 'pk', 'task', 'author', 'compiled'
