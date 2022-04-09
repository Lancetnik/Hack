from rest_framework.views import APIView
from rest_framework.response import Response

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
