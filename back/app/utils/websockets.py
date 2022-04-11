import json

from django.conf import settings

import grpc
import requests

from .grpc import websockets_pb2, websockets_pb2_grpc


def send_to_user_grpc(user_id: int, message):
    with grpc.insecure_channel('0.0.0.0:8002') as channel:
        stub = websockets_pb2_grpc.SenderStub(channel)
        response = stub.SendMessage(websockets_pb2.Message(
            message=json.dumps({
                'cliend_id': user_id,
                'message': message
            })
        ))



def send_to_group_grpc(group: str, message):
    with grpc.insecure_channel('0.0.0.0:8002') as channel:
        stub = websockets_pb2_grpc.SenderStub(channel)
        response = stub.SendMessage(websockets_pb2.Message(
            message=json.dumps({
                'room': group,
                'message': message
            })
        ))


def send_to_user_http(user_id: int, message: dict):
    return requests.post(
        f'{settings.WEBSOCKETS_URL}/user',
        json={
            "message": message,
            "user_id": user_id
        }
    )


def send_to_group_http(group: str, message: dict):
    return requests.post(
        f'{settings.WEBSOCKETS_URL}/room',
        json={
            "message": message,
            "room": group
        }
    )
