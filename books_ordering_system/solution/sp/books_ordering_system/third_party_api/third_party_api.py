"""
Name : third_party_api.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 1:19 PM
Desc: third_party_api.py
"""
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.third_party_api.exceptions import \
    APIException
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.third_party_api.third_party_api\
    import ThirdPartyAPIServiceSPI


class TPAPIServiceSP(ThirdPartyAPIServiceSPI):

    def __init__(self, api_endpoint: str):
        self._api_endpoint = api_endpoint

    def get_books_details(self, isbn_no: str):
        try:
            print("API invocation logic goes here")
        except Exception as e:
            raise APIException(message="Error occurred while invoking the API. {}".format(str(e)))

