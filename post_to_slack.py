import requests
import os
import json
from tabulate import tabulate
from get_share_price import get_share_prices
from dotenv import load_dotenv

load_dotenv()


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
