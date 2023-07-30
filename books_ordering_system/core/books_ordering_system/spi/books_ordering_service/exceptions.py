"""
Name : exceptions.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 2:26 PM
Desc: exceptions.py
"""


class NoProfileFoundError(Exception):

    def __init__(self, message: str):
        self._message = message
        super(NoProfileFoundError, self).__init__(self._message)

    def __repr__(self):
        return self._message
