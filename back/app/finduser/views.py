from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PhotoSerializer
from .find_api.finder import finder

class FindUsersView(APIView):
    serializer_class = PhotoSerializer

    def post(self, request):
        image = request.data['image']
        return Response(finder.find_users(image))
        

