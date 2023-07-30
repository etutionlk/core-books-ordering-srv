"""
Name : exceptions.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 12:48 PM
Desc: exceptions.py
"""


class FileUploadExeption(Exception):

    def __init__(self, message: str):
        self._message = message
        super(FileUploadExeption, self).__init__(self._message)

    def __repr__(self):
        return self._message


class FileDownloadExeption(Exception):

    def __init__(self, message: str):
        self._message = message
        super(FileDownloadExeption, self).__init__(self._message)

    def __repr__(self):
        return self._message
