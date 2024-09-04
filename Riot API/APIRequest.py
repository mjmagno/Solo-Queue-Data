
import requests


def request(api_url):
    resp = requests.get(api_url)
    data = resp.json()
    return data

