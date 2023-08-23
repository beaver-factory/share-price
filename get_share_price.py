import requests
import json
import os
import datetime as DT
from dotenv import load_dotenv

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
