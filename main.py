import json
from html_tools import generate_html_string
from api import get_share_prices, send_share_email, post_message_to_slack


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_share_prices()

    html_data_string, changes = generate_html_string(share_price)

    for user in users:
        send_share_email(user, html_data_string)

    post_message_to_slack(share_price, changes)


main()
