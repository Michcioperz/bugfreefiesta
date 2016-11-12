from django.core.management.base import BaseCommand
from bugfreefiesta.models import Task, Test, PinTest, Submission, Result, PinResult

class Command(BaseCommand):
    def handle(self, *args, **options):
        pass
