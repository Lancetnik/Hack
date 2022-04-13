from django.core.cache import cache
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
            get_phone_data(request.data['phone']),
            status=status.HTTP_200_OK
        )


class GetCacheView(APIView):

    def get(self, request):
        return Response({
            'photo_coordinates':cache.get('photo_coordinates'),
            'social_vk': cache.get('social_vk'),
            'phone_coordinates': cache.get('phone_coordinate')
                    })


class CleanCacheView(APIView):

    def get(self, request):
        cache.set('photo_coordinates', ''),
        cache.set('social_vk', ''),
        cache.set('phone_coordinate', '')
        return Response(200)
