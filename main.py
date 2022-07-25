import os
import requests
import argparse

from urllib.parse import urlparse
from dotenv import load_dotenv


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', type=str)
    args = parser.parse_args()
    user_link = args.link
    return user_link


def shorten_link(api_bitlink_token, user_link):
    url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {
        "Authorization": f"Bearer {api_bitlink_token}"
    }
    payload = {
        "long_url": user_link,
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return bitlink


def is_bitlink(api_bitlink_token, prepared_url):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{prepared_url}'
    headers = {
        "Authorization": f"Bearer {api_bitlink_token}"
    }
    response = requests.get(url, headers=headers)
    return response.ok


def count_clicks(api_bitlink_token, bitlink):
    headers = {
        'Authorization': f'Bearer {api_bitlink_token}'
    }
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary',
        headers=headers
    )
    response.raise_for_status()
    clicks_count = response.json()["total_clicks"]
    return clicks_count


def main():
    load_dotenv()
    api_bitlink_token = os.environ['API_BITLINK_TOKEN']
    user_link = createParser()
    parsed_url = urlparse(user_link)
    prepared_url = f'{parsed_url.netloc}{parsed_url.path}'
    try:
        if is_bitlink(api_bitlink_token, prepared_url):
            clicks_count = count_clicks(api_bitlink_token, prepared_url)
            print(clicks_count)
        else:
            bitlink = shorten_link(api_bitlink_token, user_link)
            print('Битлинк', bitlink)
    except requests.exceptions.HTTPError:
        print("Ошибка. Ссылка некорректная")


if __name__ == "__main__":
    main()
