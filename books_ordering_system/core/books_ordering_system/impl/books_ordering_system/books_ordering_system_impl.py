"""
Name : books_ordering_system_impl.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 1:39 PM
Desc: books_ordering_system_impl.py
"""
from books_ordering_system.core.books_ordering_system.api.books_ordering_system.books_ordering_system import \
    BooksOrderingSystem
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_ordering_service_registry \
    import BooksOrderingRegistry


class BooksOrderingSystemImpl(BooksOrderingSystem):

    def __init__(self, books_registry: BooksOrderingRegistry):
        self._books_registry = books_registry

    def run_ordering_system(self):
        self._books_registry.get_books_data_store().get_all_books()
        self._books_registry.get_storage_service().upload_file(file_name="tst_file", container_name="test_container")
        self._books_registry.get_third_party_api_service().get_books_details(isbn_no="ISBN-012012-1011")

