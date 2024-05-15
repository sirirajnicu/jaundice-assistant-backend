import os
import argparse
import random
import string
from datetime import datetime


def write_secret(file_path: str, content: str):
    if os.path.exists(file_path):
        return

    with open(file_path, "w") as f:
        f.write(content)


def random_string(k: int):
    valid_string = string.ascii_letters + string.digits + string.punctuation
    return f"{datetime.now().timestamp()}-{''.join([random.choice(valid_string) for _ in range(k)])}"


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--dev", action="store_true", help="Set up development environment")
    args = args_parser.parse_args()

    if args.dev:
        write_secret("./secrets/db_password.txt", "postgres")
        write_secret("./secrets/django_secrets.txt", "secretkey")
    else:
        write_secret("./secrets/db_password.txt", random_string(40))
        write_secret("./secrets/django_secrets.txt", random_string(40))
