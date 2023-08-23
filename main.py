import json
from send_share_email import send_share_email


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    for user in users:
        send_share_email(user)
