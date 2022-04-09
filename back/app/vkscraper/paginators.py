from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.utils.urls import replace_query_param


class VkPaginator(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'count'
    max_page_size = 10

    def __init__(self, *args, page_size=1, **kwargs):
        super().__init__(*args, **kwargs)
        self.page_size = page_size

    def pagination_data(self, request, view=None) -> ('size', 'number'):
        self.request = request
        self.page_size = int(self.get_page_size(request))
        paginator = self.django_paginator_class([], self.page_size)
        self.page_number = int(self.get_page_number(request, paginator))
        return self.page_size, self.page_number

    def get_paginated_response(self, data):
        url = self.request.build_absolute_uri()

        if self.page_number * self.page_size < int(data['count']):
            next_page = replace_query_param(url, self.page_query_param, self.page_number + 1)
        else:
            next_page = None

        if self.page_number > 1:
            previous_page = replace_query_param(url, self.page_query_param, self.page_number - 1)
        else:
            previous_page = None

        return {
            "next": next_page,
            "previous": previous_page,
            "count": data['count'],
            "data": data['items'],
        }
