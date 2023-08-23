import os
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv


load_dotenv()


def send_share_emails():
    with open('users.json', 'r') as f:
        users = json.load(f)

    for user in users:
        send_share_email(user)


def send_share_email(user_email):
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

    share_price = "alex func"

    message = Mail(
        from_email='teyah.brennen-davies@northcoders.com',
        to_emails=user_email,
        subject='Your NC Share Price Update',
        html_content=f'<strong>This is a share price: {share_price}</strong>')

    sg = SendGridAPIClient(SENDGRID_API_KEY)

    response = sg.send(message)

    print(response.status_code, response.body, response.headers)


send_share_emails()
