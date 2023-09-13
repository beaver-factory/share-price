from bs4 import BeautifulSoup


def calculate_price_change(current_price, last_price):
    diff = current_price-last_price

    return (diff/last_price)*100


def calculate_absolute_change(current_price, last_price):
    return current_price-last_price


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
