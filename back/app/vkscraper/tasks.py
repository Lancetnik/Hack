from typing import Optional

from config.celery import app
from utils.websockets import send_to_user_grpc

from .services.vk import get_user_posts


@app.task
def parse_user_posts(user_id: int, number: Optional[int] = None, socket_id: Optional[int] = None):
    if number is None:
        posts = True

        offset = 0
        count = 100
        while posts:
            try:
                posts = get_user_posts(user_id, offset, count)['items']
            except Exception:
                return

            offset += count

            if socket_id is not None:
                send_to_user_grpc(socket_id, posts)

    else:
        offset = 0
        count = 100
        while offset < number:
            try:
                posts = get_user_posts(user_id, offset, count)['items']
            except Exception:
                return

            offset += count

            if socket_id is not None:
                send_to_user_grpc(socket_id, posts)
