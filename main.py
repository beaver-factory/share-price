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
    <table>
    <tr><th>Time Period</th><th>Share Price</th><th>% Change</th><th>£ Change</th></tr>
    <tr><td>Today</td><td>{share_price["day"]}</td><td>0</td><td>£0</td></tr>
    <tr><td>Last Week</td><td>{share_price["week"]}</td><td>{week_change}</td><td>£{week_change_abs}</td></tr>
    <tr><td>Last 28 Days</td><td>{share_price["month"]}</td><td>{month_change}</td><td>£{month_change_abs}</td></tr>
    <tr><td>Last 6 Months</td><td>{share_price["half_year"]}</td><td>{half_change}</td><td>£{half_change_abs}</td></tr>
    <tr><td>Last Year</td><td>{share_price["year"]}</td><td>{year_change}</td><td>£{year_change_abs}</td></tr>
    </table>"""

    for user in users:
        send_share_email(user, html_data_string)


main()
