import json
from send_share_email import send_share_email
from utils import calculate_price_change, calculate_absolute_change
from get_share_price import get_share_prices
from post_to_slack import post_message_to_slack


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_share_prices()

    week_change = round(calculate_price_change(
        share_price["day"], share_price["week"]), 2)
    week_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["week"]), 2)

    month_change = round(calculate_price_change(
        share_price["day"], share_price["month"]), 2)
    month_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["month"]), 2)

    half_change = round(calculate_price_change(
        share_price["day"], share_price["half_year"]), 2)
    half_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["half_year"]), 2)

    year_change = round(calculate_price_change(
        share_price["day"], share_price["year"]), 2)
    year_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["year"]), 2)
    
    changes = {
        week_change, week_change_abs, month_change, month_change_abs, half_change, half_change_abs, year_change, year_change_abs
    }

    html_data_string = f"""
    <h3>The current share price is: £{share_price["day"]}</h3>
    <table border='1' style='border-collapse:collapse;'>
    <tr>
        <th style="padding: 10px">Time Period</th>
        <th style="padding: 10px">Share Price</th>
        <th style="padding: 10px">% Change</th>
        <th style="padding: 10px">£ Change</th>
    </tr>
    <tr>
        <td style="padding: 10px;">Today</td>
        <td style="padding: 10px;">{share_price["day"]}</td>
        <td style="padding: 10px;">0</td>
        <td style="padding: 10px;">£0</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last Week</td>
        <td style="padding: 10px;">{share_price["week"]}</td>
        <td style="padding: 10px;">{week_change}</td>
        <td style="padding: 10px;">£{week_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last 28 Days</td>
        <td style="padding: 10px;">{share_price["month"]}</td>
        <td style="padding: 10px;">{month_change}</td>
        <td style="padding: 10px;">£{month_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last 6 Months</td>
        <td style="padding: 10px;">{share_price["half_year"]}</td>
        <td style="padding: 10px;">{half_change}</td>
        <td style="padding: 10px;">£{half_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last Year</td>
        <td style="padding: 10px;">{share_price["year"]}</td>
        <td style="padding: 10px;">{year_change}</td>
        <td style="padding: 10px;">£{year_change_abs}</td>
    </tr>
    </table>
    """

    for user in users:
        send_share_email(user, html_data_string)

    post_message_to_slack(share_price, changes)


main()
