from Findclone import FindcloneApi, is_image
from PIL import Image
from django.core.cache import cache

from django.conf import settings


class Finder:
    def __init__(self, phone, password):
        self.f = FindcloneApi()
        self.f.login(phone, password)

    def find_users(self, image):
        im1 = Image.open(image)
        im1 = im1.save("geeks.jpg")
        profiles = self.f.upload("geeks.jpg")
        resp = []
        top = True
        for profile in profiles:
            resp.append({
                'url': profile.url,
                'score': profile.score,
                'name': profile.firstname,
                'photo': profile.raw_details[0]['url']
            })
            if top:
                cache.set('social_vk', {
                        'url': profile.url,
                        'score': profile.score,
                        'name': profile.firstname,
                        'photo': profile.raw_details[0]['url']
                    })
            top = False
        return resp


finder = Finder(settings.FIND_LOGIN, settings.FIND_PASSWORD)
