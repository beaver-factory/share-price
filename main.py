import json
from send_share_email import send_share_email
from utils import calculate_price_change, calculate_absolute_change
from get_share_price import get_share_prices


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_share_prices()

    week_change = calculate_price_change(
        share_price["day"], share_price["week"])
    week_change_abs = calculate_absolute_change(
        share_price["day"], share_price["week"])

    month_change = calculate_price_change(
        share_price["day"], share_price["month"])
    month_change_abs = calculate_absolute_change(
        share_price["day"], share_price["month"])

    half_change = calculate_price_change(
        share_price["day"], share_price["half_year"])
    half_change_abs = calculate_absolute_change(
        share_price["day"], share_price["half_year"])

    year_change = calculate_price_change(
        share_price["day"], share_price["year"])
    year_change_abs = calculate_absolute_change(
        share_price["day"], share_price["year"])

    html_data_string = f"""
    <h3>The current share price is: {share_price["day"]}</h3>
    <table border='1' style='border-collapse:collapse; padding:10px;'>
    <tr><th>Time Period</th><th>Share Price</th><th>% Change</th><th>£ Change</th></tr>
    <tr><td style="padding: 10px;">Today</td><td style="padding: 10px;">{share_price["day"]}</td><td style="padding: 10px;">0</td><td style="padding: 10px;">£0</td></tr>
    <tr><td style="padding: 10px;">Last Week</td><td style="padding: 10px;">{share_price["week"]}</td><td style="padding: 10px;">{week_change}</td><td style="padding: 10px;">£{week_change_abs}</td></tr>
    <tr><td style="padding: 10px;">Last 28 Days</td><td style="padding: 10px;">{share_price["month"]}</td><td style="padding: 10px;">{month_change}</td><td style="padding: 10px;">£{month_change_abs}</td></tr>
    <tr><td style="padding: 10px;">Last 6 Months</td><td style="padding: 10px;">{share_price["half_year"]}</td><td style="padding: 10px;">{half_change}</td><td style="padding: 10px;">£{half_change_abs}</td></tr>
    <tr><td style="padding: 10px;">Last Year</td><td style="padding: 10px;">{share_price["year"]}</td><td style="padding: 10px;">{year_change}</td><td style="padding: 10px;">£{year_change_abs}</td></tr>
    </table>"""

    for user in users:
        send_share_email(user, html_data_string)


main()
