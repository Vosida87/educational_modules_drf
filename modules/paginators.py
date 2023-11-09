from rest_framework.pagination import PageNumberPagination


class ModulePaginator(PageNumberPagination):
    """
    PageNumberPagination - разбивает данные на страницы
    """
    page_size = 10  # Выводим по 10 модулей
