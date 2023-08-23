import json
from send_share_email import send_share_email
from get_share_price import get_latest_closing_share_price
from utils.utils import calculate_price_change


def main():
    with open('users.json', 'r') as f:
        users = json.load(f)

    share_price = get_latest_closing_share_price()

    week_change = calculate_price_change(share_price.day, share_price.week)
    month_change = calculate_price_change(share_price.day, share_price.month)
    half_change = calculate_price_change(
        share_price.day, share_price.half_year)
    year_change = calculate_price_change(share_price.day, share_price.year)

    html_data_string = f'<h2>Your Northcoders share price update for today!</h2><h3>The current share price is: {share_price.day}</h3><table><tr><th>Time Period</th><th>Price</th><th>% Change</th></tr><tr><td>Today</td><td>{share_price.day}</td><td>0</td></tr><tr><td>Last Week</td><td>{share_price.week}</td><td>{week_change}%</td></tr><tr><td>Last 28 Days</td><td>{share_price.month}</td><td>{month_change}%</td></tr><tr><td>Last 6 Months</td><td>{share_price.half_year}</td><td>{half_change}</td></tr><tr><td>Last Year</td><td>{share_price.year}</td><td>{year_change}</td></tr></table>'

    for user in users:
        send_share_email(user, html_data_string)


main()
