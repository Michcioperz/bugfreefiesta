from django.core.management.base import BaseCommand
from django.db import models
from bugfreefiesta.models import Task, Test, PinTest, Submission, Result, PinResult
import subprocess, os

class Command(BaseCommand):
    def handle(self, *args, **options):
        for to_compile in Submission.objects.filter(compiled=False):
            compiler = subprocess.run(['g++', '-x', 'c++', '-std=c++11', '-O2', '-o', os.path.join(os.getenv("VIRTUAL_ENV", "/home/michcioperz"), "compiled", "{}.o".format(to_compile.pk)), '-'], universal_newlines=True, input=to_compile.code, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            to_compile.code = ""
            to_compile.compiled = True
            to_compile.compilator_output = "Return code {}\n".format(compiler.returncode) + compiler.stdout
            if compiler.returncode:
                for test in to_compile.task.tests.all():
                    Result.objects.create(submission=to_compile, test=test, return_type="CE", time=0)
            to_compile.save()
        for task in Task.objects.filter(enabled=True):
            for submission in task.submissions.annotate(results__count=models.Count('results')).filter(results__count__lt=task.tests.count()):
                for test in task.tests.exclude(results__submission=submission):
                    try:
                        result = subprocess.run(['/usr/bin/time', '-o', os.path.join(os.getenv("VIRTUAL_ENV", "/home/michcioperz"), "results", "s{}t{}.time".format(submission.pk, test.pk)), os.path.join(os.getenv("VIRTUAL_ENV", "/home/michcioperz"), "compiled", "{}.o".format(submission.pk))], universal_newlines=True, input=test.cin, timeout=5, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
                        with open(os.path.join(os.getenv("VIRTUAL_ENV", "/home/michcioperz"), "results", "s{}t{}.time".format(submission.pk, test.pk))) as tfile:
                            correctness = eval(task.custom_comparator, locals=dict(cout=result.stdout, solution=test.cout)) if task.custom_comparator_enabled else (result.stdout.strip() == test.cout.strip())
                            Result.objects.create(time=sum([float(x) for x in tfile.read().split(" ", 2)[:2]]), result_type=("AC" if correctness else "WA"), submission=submission, test=test)
                    except subprocess.TimeoutExpired:
                        Result.objects.create(submission=submission, test=test, result_type="TLE", time=5)
                    except subprocess.CalledProcessError:
                        Result.objects.create(submission=submission, test=test, result_type="XE", time=5)
