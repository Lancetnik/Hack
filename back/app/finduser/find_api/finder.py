from Findclone import FindcloneApi, is_image
from PIL import Image 
import PIL 

from config.settings import FIND_LOGIN, FIND_PASSWORD

class Finder:

    def __init__(self, phone, password):
        self.f = FindcloneApi()
        self.f.login(phone, password)

    def find_users(self, image):
        im1 = Image.open(image) 
        im1 = im1.save("geeks.jpg")
        profiles = self.f.upload("geeks.jpg")
        resp = []
        for profile in profiles:
            resp.append(
                {
                    'url':profile.url, 
                    'score':profile.score,
                    'name':profile.firstname,
                    'photo':profile.raw_details[0]['url']
                }
            )
        return resp

finder = Finder(FIND_LOGIN, FIND_PASSWORD)