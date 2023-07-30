"""
Name : exceptions.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 1:22 PM
Desc: exceptions.py
"""


class APIException(Exception):

    def __init__(self, message: str):
        self._message = message
        super(APIException, self).__init__(self._message)

    def __repr__(self):
        return self._message
