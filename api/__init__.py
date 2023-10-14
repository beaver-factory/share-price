import requests
import json
import os
import datetime as DT
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from html_tools import insert_into_html
from tabulate import tabulate

load_dotenv()


def get_share_prices():
    # use this request to inspect response body without using up API limit:

    # response = requests.get(
    #     'https://eodhistoricaldata.com/api/eod/MCD.US?api_token=demo&fmt=json')

    response = requests.get(
        f'https://eodhistoricaldata.com/api/eod/CODE.LSE?api_token={os.getenv("EOD_API_KEY")}&fmt=json')

    parsed_response = json.loads(response.content)
    week_index = get_date_index(parsed_response, 1)
    month_index = get_date_index(parsed_response, 4)
    half_year_index = get_date_index(parsed_response, 26)

    day_closing_price = parsed_response[-1]['close']
    week_closing_price = parsed_response[week_index]['close']
    month_closing_price = parsed_response[month_index]['close']
    half_year_closing_price = parsed_response[half_year_index]['close']
    year_closing_price = parsed_response[0]['close']

    prices = {"day": day_closing_price, "week": week_closing_price, "month": month_closing_price,
              "half_year": half_year_closing_price, "year": year_closing_price}

    return prices


def get_date_index(parsed_response, num_weeks):
    today = DT.date.today()
    week_ago = today - DT.timedelta(weeks=num_weeks)
    week_str = week_ago.strftime('%Y-%m-%d')

    week_index = 0
    for idx, x in enumerate(parsed_response):
        if x['date'] == week_str:
            week_index = idx
            break

    return week_index


def send_share_email(user_email, html_data_string):
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")

    email_body = insert_into_html('email_copy.html', html_data_string)

    message = Mail(
        from_email='teyah.brennen-davies@northcoders.com',
        to_emails=user_email,
        subject='Your NC Share Price Update!',
        html_content=email_body
    )

    sg = SendGridAPIClient(SENDGRID_API_KEY)

    response = sg.send(message)

    print(response.status_code, response.body, response.headers)


def post_message_to_slack(share_price, changes):

    copy = f"""
    Here's your stock report!\n\n
    The current share price is: {share_price["day"]}\n\n
    
    {tabulate([
        ['Today', share_price["day"], 0, "£0"],
        ['Last Week', share_price['week'], changes['week_change'], f"{changes['week_change_abs']}"],
        ['Last 28 Days', share_price['month'], changes['month_change'], f"£{changes['month_change_abs']}"],
        ['Last 6 months', share_price['half_year'], changes['half_change'], f"£{changes['half_change_abs']}"],
        ['Last Year', share_price['year'], changes['year_change'], f"£{changes['year_change_abs']}"]
    ], headers=['Time Period', 'Share Price', '% Change', '£ Change'])}
    """
    return requests.post(os.getenv("WEBHOOK_URL"), json.dumps({"channel": "nc-shares", "text": copy}))