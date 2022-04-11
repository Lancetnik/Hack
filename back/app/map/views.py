from rest_framework.views import APIView
from rest_framework.response import Response
from PIL import Image
from loguru import logger

from .serializers import PointSerializer


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
        # logger.debug(request.data['file'])
        im.save(fp='./image.jpg')

