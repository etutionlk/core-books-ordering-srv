"""
Name : books_data_store.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 6:47 AM
Desc: books_data_store.py
"""
from abc import ABC, abstractmethod
from books_ordering_system.core.books_ordering_system.api.books_ordering_system.dto.book import Book


class BooksDataStoreSPI(ABC):

    @abstractmethod
    def get_all_books(self):
        pass

    @abstractmethod
    def save_book(self, book: Book):
        pass
