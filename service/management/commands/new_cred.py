from django.core.management.base import BaseCommand
from django.utils import timezone
from core.settings import DEBUG
import secrets
import string
import yaml


class Command(BaseCommand):
    help = "Create new config file with new secret key inside"

    def handle(self, *args, **options):
        valid_string: str = string.ascii_letters + string.punctuation + string.digits
        CRED = yaml.load(open("cred.yaml"), Loader=yaml.Loader)
        new_key = "".join([secrets.choice(valid_string) for _ in range(50)])
        SECRET_KEY = f"secure-{timezone.now().timestamp()}-{new_key}"
        lines: list[str]= [
            # Production
            f"DEBUG: {CRED['DEBUG']}",
            f"SECRET_KEY: {SECRET_KEY}",
        ]
        with open("new_cred.yaml", mode="w", encoding="utf-8") as file:
            file.write("\n".join(lines))