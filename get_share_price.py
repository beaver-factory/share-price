import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_latest_closing_share_price():
    # use this request to inspect response body without using up API limit:

    # response = requests.get(
    #     'https://eodhistoricaldata.com/api/eod/MCD.US?api_token=demo&fmt=json')

    response = requests.get(
        f'https://eodhistoricaldata.com/api/eod/CODE.LSE?api_token={os.getenv("EOD_API_KEY")}&fmt=json')

    parsed_response = json.loads(response.content)

    latest_closing_price = parsed_response[-1]['close']

    return latest_closing_price
