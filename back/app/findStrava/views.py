import time

from rest_framework.views import APIView
from rest_framework.response import Response

from .additional.strava_utils.strava import get_route


class GetPolyline(APIView):

    def get(self, request):
        time.sleep(4)
        massline = get_route()
        return Response(massline)
