from rest_framework.pagination import PageNumberPagination

class CustomPageNumberPagination(PageNumberPagination):
    def get_page_size(self, request):
        page_size = request.query_params.get('size', None)
        return int(page_size) if page_size is not None else self.page_size