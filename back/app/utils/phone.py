import requests
import time
from django.core.cache import cache

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
    logger.debug(resp['location']['geo_city']["latitude"])
    cache.set('phone_coordinate',[float(resp['location']['geo_city']["latitude"]), float(resp['location']['geo_city']["longitude"])])
    resp.update({'point' : point.data})

    return resp