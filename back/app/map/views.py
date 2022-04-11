from rest_framework.views import APIView
from rest_framework.response import Response

from PIL import Image
import random

from .serializers import PointSerializer
from .service import *

class GetPostition(APIView):
    def get(self, request, pk):
        point = PointSerializer(data={
            "id": pk,
            "latitude": 59.937,
            "longitude": 30.3089
        })
        point.is_valid()
        return Response(point.data)


class GetLocation(APIView):
    def post(self, request):
        im = Image.open(request.data['file'])
        # im.save(fp='./data/Test/final_test_ciphered/image.jpg')
        # result_model = MODEL()
        result_model = [59.937, 31.31]
        point = PointSerializer(data={
            'id': random.randint(1, 10),
            'latitude': result_model[0],
            'longitude': result_model[1]            
        })
        point.is_valid()
        return Response(point.data)
