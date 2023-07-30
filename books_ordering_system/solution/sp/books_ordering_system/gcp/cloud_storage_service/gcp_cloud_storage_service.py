"""
Name : gcp_cloud_storage_service.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 12:58 PM
Desc: gcp_cloud_storage_service.py
"""
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_storage_service.\
    books_storage_service import BooksStorageServiceSPI
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_storage_service.exceptions \
    import FileUploadExeption, FileDownloadExeption


class GCPCloudStorageServiceSP(BooksStorageServiceSPI):

    def __init__(self, connection_str: str):
        self._connection_str = connection_str

    def upload_file(self, file_name: str, container_name: str):
        try:
            print("GCP Cloud file uploading logic handling code goes here")
        except Exception as e:
            raise FileUploadExeption(message="Error occurred while uploading a file. {}".format(str(e)))

    def download_file(self, file_name: str):
        try:
            print("GCP Cloud file downloading logic handling code goes here")
        except Exception as e:
            raise FileDownloadExeption(message="Error occurred while downloading a file. {}".format(str(e)))