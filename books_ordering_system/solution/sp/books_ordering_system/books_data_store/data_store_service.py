"""
Name : data_store_service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 1:02 PM
Desc: data_store_service.py
"""
from books_ordering_system.core.books_ordering_system.api.books_ordering_system.dto.book import Book
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_data_store.books_data_store\
    import BooksDataStoreSPI
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_data_store.exceptions import \
    DatabaseConnectionException


class DataStoreSP(BooksDataStoreSPI):

    def __init__(self, db_connection_str: str, ssl_cert_path: str):
        self._db_connection_str = db_connection_str
        self._ssl_cert_path = ssl_cert_path

    def get_all_books(self):
        try:
            print("database record fetching logic goes here")
        except Exception as e:
            raise DatabaseConnectionException(message="Error occurred while connecting to the db. {}".format(str(e)))

    def save_book(self, book: Book):
        try:
            print("saving records to the database logic code goes here")
        except Exception as e:
            raise DatabaseConnectionException(message="Error occurred while connecting to the db. {}".format(str(e)))

