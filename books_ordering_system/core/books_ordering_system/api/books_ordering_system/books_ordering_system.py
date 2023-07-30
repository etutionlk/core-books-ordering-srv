"""
Name : books_ordering_system.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 1:32 PM
Desc: books_ordering_system.py
"""
from abc import abstractmethod, ABC


class BooksOrderingSystem(ABC):

    @abstractmethod
    def run_ordering_system(self):
        pass
