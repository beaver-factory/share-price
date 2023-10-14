from utils import calculate_price_change, calculate_absolute_change
from bs4 import BeautifulSoup


def insert_into_html(base_path, copy):
    with open(base_path, 'r', encoding='utf-8') as html_file:
        base_content = html_file.read()

    soup = BeautifulSoup(base_content, 'html.parser')

    found_element = soup.find(id='stock_data_2023')

    if found_element:
        new_tag = soup.new_tag("div")
        new_tag.append(BeautifulSoup(copy, 'html.parser'))
        found_element.append(new_tag)
        amended_html = soup.prettify()

        return amended_html
    else:
        print("Element not found.")


def merge_html(base_path, new_path):
    with open(base_path, 'r', encoding='utf-8') as html_file:
        base_content = html_file.read()

    with open(new_path, 'r', encoding='utf-8') as html_file:
        new_content = html_file.read()

    soup = BeautifulSoup(base_content, 'html.parser')

    found_element = soup.find(id='stock_data_2023')

    if found_element:
        new_html = new_content
        new_tag = soup.new_tag("div")
        new_tag.append(BeautifulSoup(new_html, 'html.parser'))
        found_element.append(new_tag)
        amended_html = soup.prettify()

        return amended_html
    else:
        print("Element not found.")


def generate_row(timeframe, share_price, percent_change, abs_change):
    return f"""
    <tr>
        <td style="padding: 10px;">{timeframe}</td>
        <td style="padding: 10px;">£{share_price}</td>
        <td style="padding: 10px; color: {'green' if percent_change > 0 else 'red'};">{percent_change}%</td>
        <td style="padding: 10px; color: {'green' if abs_change > 0 else 'red'};">£{abs_change}</td>
    </tr>"""


def generate_html_string(share_price):
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

    changes = {
        "week_change": week_change, "week_change_abs": week_change_abs, "month_change": month_change, "month_change_abs": month_change_abs, "half_change": half_change, "half_change_abs": half_change_abs, "year_change": year_change, "year_change_abs": year_change_abs
    }

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

    return {html_data_string, changes}
