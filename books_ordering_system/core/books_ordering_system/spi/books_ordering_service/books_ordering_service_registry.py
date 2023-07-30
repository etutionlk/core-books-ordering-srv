"""
Name : books_ordering_service_registry.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 6:45 AM
Desc: books_ordering_service_registry.py
"""
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_data_store.books_data_store\
    import BooksDataStoreSPI
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_storage_service.\
    books_storage_service import BooksStorageServiceSPI
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.third_party_api.third_party_api\
    import ThirdPartyAPIServiceSPI


class BooksOrderingRegistry:

    def __init__(self, books_data_store: BooksDataStoreSPI,
                 storage_service: BooksStorageServiceSPI,
                 third_party_api: ThirdPartyAPIServiceSPI):
        self._books_data_store = books_data_store
        self._storage_service = storage_service
        self._third_party_api = third_party_api

    def get_books_data_store(self) -> BooksDataStoreSPI:
        return self._books_data_store

    def get_storage_service(self) -> BooksStorageServiceSPI:
        return self._storage_service

    def get_third_party_api_service(self) -> ThirdPartyAPIServiceSPI:
        return self._third_party_api
