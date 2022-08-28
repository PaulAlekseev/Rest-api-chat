from rest_framework.pagination import PageNumberPagination


class MessagePagination(PageNumberPagination):
    page_size = 3
    max_page_size = 30
    page_size_query_param = 'page_size'


class TopicPagination(PageNumberPagination):
    page_size = 10
    max_page_size = 20
    page_size_query_param = 'page_size'
