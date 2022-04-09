from django.conf import settings
from django.core.exceptions import BadRequest

import vk_api


vk_user_session = vk_api.VkApi(token=settings.VK_USER_KEY)


def search_user(q: str, offset=0, count=1):
    return vk_user_session.method('users.search', {
        'q': q,
        'offset': offset,
        'count': count,
        'fields': ','.join((
            'sex', 'bdate', 'city', 
            'country', 'about', 'domain',
            'deactivated', 'is_closed', 'activities',
            'books', 'career', 'city',
            'connections', 'contacts', 'education',
            'home_town', 'interests', 'last_seen',
            'military', 'occupation', 'personal',
            'relatives', 'relation'
        ))
    })


def get_user_posts(user_id: int, offset=0, count=100):
    try:
        return vk_user_session.method('wall.get', {
            'owner_id': user_id,
            'offset': offset,
            'filter': 'owner',
            'count': count
        })
    except vk_api.exceptions.ApiError as e:
        raise BadRequest(e)
