from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

RESULT_TYPES = {
  "WA":  "Wrong Answer",
  "TLE": "Time Limit Exceeded",
  "XE":  "Execution Error",
  "CE":  "Compilation Error",
  "AC":  "Accepted",
}

class Task(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    enabled = models.BooleanField(default=True)
    custom_comparator_enabled = models.BooleanField(default=False)
    custom_comparator = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.name, self.slug)

    def get_absolute_url(self):
        return reverse("task_detail", kwargs=dict(slug=self.slug))

class Test(models.Model):
    task = models.ForeignKey(Task, related_name="tests")
    cin = models.TextField(null=True, blank=True)
    cout = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def average_time(self):
        return self.results.filter(result_type="AC").aggregate(models.Avg(time)).get("time__avg", "NaN")

    def get_absolute_url(self):
        return reverse("test_detail", kwargs=dict(pk=self.pk))

class PinTest(models.Model):
    task = models.ForeignKey(Task, related_name="pin_tests")
    cin = models.TextField(null=True, blank=True)
    cout = models.TextField(null=True, blank=True)
    enabled = models.BooleanField(default=True)

    def average_time(self):
        return self.results.filter(result_type="AC").aggregate(models.Avg(time)).get("time__avg", "NaN")

    def get_absolute_url(self):
        return reverse("pin_test_detail", kwargs=dict(pk=self.pk))


class Submission(models.Model):
    task = models.ForeignKey(Task, related_name="submissions")
    author = models.ForeignKey(User, related_name="submissions")
    code = models.TextField(null=True, blank=True)
    compiled = models.BooleanField(default=False)
    compilator_output = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def average_time(self):
        return self.results.filter(result_type="AC").aggregate(models.Avg(time)).get("time__avg", "NaN")

    def average_instructions(self):
        return self.pin_results.filter(result_type="AC").aggregate(models.Avg(time)).get("time__avg", "NaN")

    def accepted_timed(self):
        return self.results.filter(result_type="AC").count()

    def accepted_counted(self):
        return self.pin_results.filter(result_type="AC").count()

    def get_absolute_url(self):
        return reverse("submission_detail", kwargs=dict(pk=self.pk))

class Result(models.Model):
    submission = models.ForeignKey(Submission, related_name="results")
    test = models.ForeignKey(Test, related_name="results")
    result_type = models.CharField(max_length=3, choices=list(RESULT_TYPES.items()))
    time = models.FloatField()

    def get_absolute_url(self):
        return reverse("result_detail", kwargs=dict(pk=self.pk))


class PinResult(models.Model):
    submission = models.ForeignKey(Submission, related_name="pin_results")
    pin_test = models.ForeignKey(PinTest, related_name="results")
    result_type = models.CharField(max_length=3, choices=list(RESULT_TYPES.items()))
    time = models.BigIntegerField()

    def get_absolute_url(self):
        return reverse("pin_result_detail", kwargs=dict(pk=self.pk))
