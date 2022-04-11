from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response

from utils.phone import get_phone_data

from .serializers import PhotoSerializer, PhoneSerializer
from .find_api.finder import finder


class FindUsersView(APIView):
    serializer_class = PhotoSerializer

    def post(self, request):
        image = request.data['image']
        return Response(finder.find_users(image))


class FindUserByPhone(generics.CreateAPIView):
    serializer_class = PhoneSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            get_phone_data(serializer.data['phone']),
            status=status.HTTP_200_OK
        )
