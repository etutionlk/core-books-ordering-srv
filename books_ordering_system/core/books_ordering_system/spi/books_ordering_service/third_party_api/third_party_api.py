"""
Name : third_party_api.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 6:59 AM
Desc: third_party_api.py
"""
from abc import abstractmethod, ABC


class ThirdPartyAPIServiceSPI(ABC):

    @abstractmethod
    def get_books_details(self, isbn_no: str):
        pass
