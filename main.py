import json
from send_share_email import send_share_email
from utils import calculate_price_change, calculate_absolute_change, generate_row
from get_share_price import get_share_prices


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_share_prices()

    week_change = round(calculate_price_change(
        share_price["day"], share_price["week"]), 2)
    week_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["week"])/100, 2)

    month_change = round(calculate_price_change(
        share_price["day"], share_price["month"]), 2)
    month_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["month"])/100, 2)

    half_change = round(calculate_price_change(
        share_price["day"], share_price["half_year"]), 2)
    half_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["half_year"])/100, 2)

    year_change = round(calculate_price_change(
        share_price["day"], share_price["year"]), 2)
    year_change_abs = round(calculate_absolute_change(
        share_price["day"], share_price["year"])/100, 2)

    html_data_string = f"""
    <h3>The current share price is: £{round(share_price["day"]/100, 2)}</h3>
    <table border='1' style='border-collapse:collapse;'>
    <tr>
        <th style="padding: 10px">Time Period</th>
        <th style="padding: 10px">Share Price</th>
        <th style="padding: 10px">% Change</th>
        <th style="padding: 10px">£ Change</th>
    </tr>
    <tr>
        <td style="padding: 10px;">Today</td>
        <td style="padding: 10px;">£{round(share_price["day"]/100,2)}</td>
        <td style="padding: 10px;">-</td>
        <td style="padding: 10px;">-</td>
    </tr>
    {generate_row('Last Week', round(share_price['week']/100,2), week_change, week_change_abs)}
    {generate_row('Last 28 Days', round(share_price['month']/100,2), month_change, month_change_abs)}
    {generate_row('Last 6 Months', round(share_price['half_year']/100,2), half_change, half_change_abs)}
    {generate_row('Last Year', round(share_price['year']/100,2),year_change, year_change_abs)}
    </table>
    """

    for user in users:
        send_share_email(user, html_data_string)


main()
