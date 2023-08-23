import json
from send_share_email import send_share_email
from get_share_price import get_share_prices


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_prices = get_share_prices()

    for user in users:
        send_share_email(user, share_prices)


main()
