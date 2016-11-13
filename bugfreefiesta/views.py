from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import RESULT_TYPES, Task, Test, PinTest, Submission, Result, PinResult

def task_list(request):
    tasks = get_list_or_404(Task, enabled=True)
    return render(request, "task_list.html", dict(tasks=tasks))

def task_detail(request, slug: str):
    task = get_object_or_404(Task, slug=slug, enabled=True).prefetch_related('tests', 'pin_tests', 'submissions')
    return render(request, "task_detail.html", dict(task=task))


def submission_detail(request, pk: str):
    if request.is_staff:
        submission = get_object_or_404(Submission, pk=pk)
    else:
        submission = get_object_or_404(Submission, pk=pk, author=request.user)
    return render(request, "submission_detail.html", dict(submission=submission))


class SubmissionForm(forms.Form):
    code = forms.CharField(widget=forms.widgets.Textarea)


@login_required
def task_submit(request, slug: str):
    task = get_object_or_404(Task, slug=slug, enabled=True)
    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        if form.is_valid():
            return redirect(Submission.objects.create(task=task, author=request.user, code=form.cleaned_data['code']))
    else:
        form = SubmissionForm()
    return render(request, "task_submit.html", dict(form=form, task=task))


def test_detail(request, pk: str):
    test = get_object_or_404(Test, pk=pk, enabled=True)
    return render(request, "test_detail.html", dict(test=test))


def pin_test_detail(request, pk: str):
    pin_test = get_object_or_404(PinTest, pk=pk, enabled=True)
    return render(request, "pin_test_detail.html", dict(pin_test=pin_test))


def result_detail(request, pk: str):
    if request.user.is_staff:
        result = get_object_or_404(Result, pk=pk)
    else:
        result = get_object_or_404(Result, pk=pk, submission__author=request.user)
    return render(request, "result_detail.html", dict(result=result))


def pin_result_detail(request, pk: str):
    if request.user.is_staff:
        result = get_object_or_404(PinResult, pk=pk)
    else:
        result = get_object_or_404(PinResult, pk=pk, submission__author=request.user)
    return render(request, "pin_result_detail.html", dict(pin_result=pin_result))
