import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from .utils.utils import insert_into_html

load_dotenv()


def send_share_email(user_email, share_price):
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

    email_body = insert_into_html('email_copy.html', share_price)

    message = Mail(
        from_email='teyah.brennen-davies@northcoders.com',
        to_emails=user_email,
        subject='Your NC Share Price Update!',
        html_content=email_body
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)

    response = sg.send(message)

    print(response.status_code, response.body, response.headers)
