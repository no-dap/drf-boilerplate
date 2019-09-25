from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class PostPagination(CursorPagination):
    page_size = 5
    ordering = ('id', )
