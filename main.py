import json
from html_tools import generate_html_string
from api import get_share_prices, send_share_email, post_message_to_slack
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    users_string = os.getenv("TO_EMAILS")

    users = users_string.split(', ')
    share_price = get_share_prices()

    html_data_string, changes = generate_html_string(share_price)

    for user in users:
        send_share_email(user, html_data_string)

    post_message_to_slack(share_price, changes)


main()
