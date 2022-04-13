import requests
import time

from .proxy import proxy
from map.serializers import PointSerializer

from loguru import logger


def get_phone_data(phone: str): 
    r = requests.get(
        'https://xn----7sbqamfrkhj2bc3a.com/emulator/check',
        params={
            "driver": "geo",
            "provider": "phone",
            "uid": phone
        },
        proxies=proxy.get_proxy()
    )
    resp = r.json()
    point = PointSerializer(data={
            "id": 1,
            "latitude": resp['location']['geo_city']["latitude"],
            "longitude": resp['location']['geo_city']["longitude"]
        })
    point.is_valid()
    resp.update({'point' : point.data})

    return resp