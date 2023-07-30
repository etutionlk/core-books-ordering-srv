"""
Name : books_storage_service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 7:03 AM
Desc: books_storage_service.py
"""
from abc import ABC, abstractmethod


class BooksStorageServiceSPI(ABC):

    @abstractmethod
    def upload_file(self, file_name: str, container_name: str):
        pass

    @abstractmethod
    def download_file(self, file_name: str):
        pass
