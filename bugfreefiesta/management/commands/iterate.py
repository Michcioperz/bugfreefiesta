from django.core.management.base import BaseCommand
from bugfreefiesta.models import Task, Test, PinTest, Submission, Result, PinResult
import subprocess, os

class Command(BaseCommand):
    def handle(self, *args, **options):
        for to_compile in Submission.objects.filter(compiled=False):
            compiler = subprocess.run(['g++', '-x', 'c++', '-std=c++11', '-O2', '-o', os.path.join(os.getenv("VIRTUAL_ENV", "/home/michcioperz"), "compiled", "{}.o".format(to_compile.pk)), '-'], universal_newlines=True, input=to_compile.code, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            to_compile.code = ""
            to_compile.compiled = True
            to_compile.compilator_output = "Return code {}\n".format(compiler.returncode) + compiler.stdout
            to_compile.save()
