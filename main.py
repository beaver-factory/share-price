import json
from send_share_email import send_share_email
from get_share_price import get_latest_closing_share_price


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_latest_closing_share_price()

    for user in users:
        send_share_email(user, share_price)


main()
