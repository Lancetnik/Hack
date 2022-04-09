from django.conf import settings

import requests


def send_to_user(user_id: int, message: dict):
    return requests.post(
        f'{settings.WEBSOCKETS_URL}/user',
        json={
            "message": message,
            "user_id": user_id
        }
    )


def send_to_group(group: str, message: dict):
    return requests.post(
        f'{settings.WEBSOCKETS_URL}/room',
        json={
            "message": message,
            "room": group
        }
    )
