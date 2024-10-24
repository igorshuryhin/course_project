from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'page_size'
    ordering = '-created_at'

    def get_paginated_response(self, page):
        super_response = super().get_paginated_response(page).data

        return Response({
            **super_response,
            'page_size': self.page_size
        })
