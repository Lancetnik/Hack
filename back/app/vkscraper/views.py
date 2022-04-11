from django.core.exceptions import BadRequest
from drf_yasg.utils import swagger_auto_schema
from rest_framework import views, generics, status
from rest_framework.response import Response

from .paginators import VkPaginator
from .services.vk import search_user, get_user_posts
from .serializers import (
    SearchUserRequestSerializer, PaginationSerializer,
    CeleryTaskSerializer, EmptySerializer
)
from .tasks import parse_user_posts


class FindUser(generics.RetrieveAPIView):
    paginator = VkPaginator(page_size=1)
    serializer_class = EmptySerializer

    @swagger_auto_schema(
        operation_description="Поиск пользователей ВК",
        query_serializer=SearchUserRequestSerializer
    )
    def get(self, request):
        request_data = SearchUserRequestSerializer(data=request.query_params)
        request_data.is_valid(raise_exception=True)

        size, page = self.paginator.pagination_data(self.request, view=self)
        data = search_user(request_data.data['q'], offset=(page*size), count=size)
        data = self.paginator.get_paginated_response(data)
        return Response(data, status=status.HTTP_200_OK)


class GetUserPosts(generics.RetrieveAPIView):
    paginator = VkPaginator(page_size=10)
    serializer_class = EmptySerializer

    @swagger_auto_schema(
        operation_description="Сбор постов пользователя по его ID",
        query_serializer=PaginationSerializer
    )
    def get(self, request, user_id):
        size, page = self.paginator.pagination_data(self.request, view=self)

        try:
            data = get_user_posts(user_id, offset=(page*size), count=size)
        except BadRequest as e:
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        data = self.paginator.get_paginated_response(data)
        return Response(data, status=status.HTTP_200_OK)


class GetUserPostsBackground(generics.RetrieveAPIView):
    serializer_class = EmptySerializer

    @swagger_auto_schema(
        operation_description="Запуск фоновой задачи по сбору постов пользователя",
        query_serializer=CeleryTaskSerializer
    )
    def get(self, request, user_id):
        request_data = CeleryTaskSerializer(data=request.query_params)
        request_data.is_valid(raise_exception=True)
        parse_user_posts.delay(
            user_id, request_data.data.get('number'), request_data.data.get('socket_id')
        )
        return Response(status=status.HTTP_201_CREATED)
