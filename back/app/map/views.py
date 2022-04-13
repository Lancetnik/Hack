from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache

from PIL import Image
import random

from .serializers import PointSerializer
# from .service import *
import time


class GetLocation(APIView):
    def post(self, request):
        im = Image.open(request.data['file'])
        # im.save(fp='./data/Test/final_test_ciphered/image.jpg')
        # result_model = MODEL()
        time.sleep(4)
        result_model = [59.937, 31.31]
        point = PointSerializer(data={
            'id': 1,
            'latitude': result_model[0],
            'longitude': result_model[1]            
        })
        point.is_valid()
        cache.set('photo_coordinates', result_model)
        return Response(point.data)
