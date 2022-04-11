from django.conf import settings
from random import choice


class Proxy:
    def __init__(self, proxy):
        self.proxy = proxy
    
    def get_proxy(self):
        if isinstance(self.proxy, list):
            return {'http': choice(self.proxy)}
        elif isinstance(self.proxy, str):
            return {'http': self.proxy}


proxy = Proxy(settings.PROXIE)
