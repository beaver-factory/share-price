import json
from send_share_email import send_share_email
from utils import calculate_price_change, calculate_absolute_change
from get_share_price import get_share_prices


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
        <td style="padding: 10px; color: {'green' if week_change > 0 else 'red'};">{week_change}</td>
        <td style="padding: 10px; {'green' if week_change_abs > 0 else 'red'};">£{week_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last 28 Days</td>
        <td style="padding: 10px;">{share_price["month"]}</td>
        <td style="padding: 10px; {'green' if month_change > 0 else 'red'};">{month_change}</td>
        <td style="padding: 10px; {'green' if month_change_abs > 0 else 'red'};">£{month_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last 6 Months</td>
        <td style="padding: 10px;">{share_price["half_year"]}</td>
        <td style="padding: 10px; {'green' if half_change > 0 else 'red'};">{half_change}</td>
        <td style="padding: 10px; {'green' if half_change_abs > 0 else 'red'};">£{half_change_abs}</td>
    </tr>
    <tr>
        <td style="padding: 10px;">Last Year</td>
        <td style="padding: 10px;">{share_price["year"]}</td>
        <td style="padding: 10px; {'green' if year_change > 0 else 'red'};">{year_change}</td>
        <td style="padding: 10px; {'green' if year_change_abs > 0 else 'red'};">£{year_change_abs}</td>
    </tr>
    </table>
    """

    for user in users:
        send_share_email(user, html_data_string)


main()
