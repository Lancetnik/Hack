from rest_framework import views, generics, status
from rest_framework.response import Response

from .paginators import VkPaginator
from .services.vk import search_user, get_user_posts
from .tasks import parse_user_posts


class FindUser(generics.RetrieveAPIView):
    paginator = VkPaginator(page_size=1)

    def get(self, request):
        if (q := self.request.query_params.get('q')) is None:
            return Response(
                '`q` as a query parameter is required',
                status=status.HTTP_400_BAD_REQUEST
            )

        size, page = self.paginator.pagination_data(self.request, view=self)
        data = search_user(q, offset=(page*size), count=size)
        data = self.paginator.get_paginated_response(data)
        return Response(data, status=status.HTTP_200_OK)


class GetUserPosts(generics.RetrieveAPIView):
    paginator = VkPaginator(page_size=10)

    def get(self, request, user_id):
        size, page = self.paginator.pagination_data(self.request, view=self)
        data = get_user_posts(user_id, offset=(page*size), count=size)
        data = self.paginator.get_paginated_response(data)
        return Response(data, status=status.HTTP_200_OK)


class GetUserPostsBackground(generics.RetrieveAPIView):
    def get(self, request, user_id):
        number = self.request.query_params.get('number')
        if number: number = int(number)
        parse_user_posts.delay(user_id, number)
        return Response(status=status.HTTP_201_OK)
