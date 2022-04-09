from typing import Optional

from config.celery import app

from .services.vk import get_user_posts


@app.task
def parse_user_posts(user_id: int, number: Optional[int] = None):
    if number is None:
        posts = True

        offset = 0
        count = 100
        while posts:
            posts = get_user_posts(user_id, offset, count)['items']
            offset += count
    
    else:
        offset = 0
        count = 100
        while offset < number:
            posts = get_user_posts(user_id, offset, count)['items']
            offset += count
