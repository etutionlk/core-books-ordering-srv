"""
Name : abstract_profile.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 28/07/2023 8:03 PM
Desc: abstract_profile.py
"""
from abc import abstractmethod, ABC


class BookOrderingProfile(ABC):

    @abstractmethod
    def get_profile_name(self):
        pass

    @abstractmethod
    def get_book_ordering_service(self):
        pass
