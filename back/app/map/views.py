from rest_framework.views import APIView
from rest_framework.response import Response


class GetPostition(APIView):
    def post(self, request):
        return Response({
            "x": 1,
            "y": 1
        })
