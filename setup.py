import secrets
import yaml
import string
import os
import datetime


if __name__ == "__main__":
    valid_string: str = string.ascii_letters + string.punctuation + string.digits
    CRED = {"DEBUG": False}
    if os.path.exists("cred.yaml"):
        CRED = yaml.load(open("cred.yaml"), Loader=yaml.Loader)

    new_key = "".join([secrets.choice(valid_string) for _ in range(50)])
    SECRET_KEY = f"secure-{datetime.datetime.now().timestamp()}-{new_key}"
    lines: list[str] = [
        # Production
        f"DEBUG: {CRED['DEBUG']}",
        f"SECRET_KEY: {SECRET_KEY}",
    ]
    with open("new_cred.yaml", mode="w", encoding="utf-8") as file:
        file.write("\n".join(lines))
