import requests

from .proxy import proxy


def get_phone_data(phone: str):  # с 7...
    r = requests.get(
        'https://xn----7sbqamfrkhj2bc3a.com/emulator/check',
        params={
            "driver": "geo",
            "provider": "phone",
            "uid": phone
        },
        proxies=proxy.get_proxy()
    )
    return r.json()
