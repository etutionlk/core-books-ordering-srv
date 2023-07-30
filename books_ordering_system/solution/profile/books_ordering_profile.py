"""
Name : books_ordering_profile.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 28/07/2023 8:04 PM
Desc: books_ordering_profile.py
"""
from books_ordering_system.core.books_ordering_system.impl.books_ordering_system.books_ordering_system_impl import \
    BooksOrderingSystemImpl
from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.books_ordering_service_registry \
    import BooksOrderingRegistry
from books_ordering_system.solution.profile.abstract_profile import BookOrderingProfile
from books_ordering_system.solution.sp.books_ordering_system.aws.s3_bucket_service.aws_s3_service import \
    AWSS3StorageServiceSP
from books_ordering_system.solution.sp.books_ordering_system.azure.blob_storage_service.azure_blob_service import \
    AzureBlobStorageServiceSP
from books_ordering_system.solution.sp.books_ordering_system.books_data_store.data_store_service import DataStoreSP
from books_ordering_system.solution.sp.books_ordering_system.gcp.cloud_storage_service.gcp_cloud_storage_service import \
    GCPCloudStorageServiceSP
from books_ordering_system.solution.sp.books_ordering_system.third_party_api.third_party_api import TPAPIServiceSP


# wire services for Azure cloud provider
class BookOrderingServiceAzureProfile(BookOrderingProfile):

    def __init__(self):
        self.books_registry = BooksOrderingRegistry(
            books_data_store=DataStoreSP(db_connection_str="connection-str-to-db", ssl_cert_path="/your/cert/path1"),
            storage_service=AzureBlobStorageServiceSP(connection_str="azure-storage-service-connection-string"),
            third_party_api=TPAPIServiceSP(api_endpoint="http://tps-api-endpoint1"))

    def get_profile_name(self):
        return "az_books_ordering_service"

    def get_book_ordering_service(self):
        return BooksOrderingSystemImpl(books_registry=self.books_registry)


# wire services for AWS cloud provider
class BookOrderingServiceAWSProfile(BookOrderingProfile):

    def __init__(self):
        self.books_registry = BooksOrderingRegistry(
            books_data_store=DataStoreSP(db_connection_str="connection-str-to-db", ssl_cert_path="/your/cert/path2"),
            storage_service=AWSS3StorageServiceSP(connection_str="aws-storage-service-connection-string"),
            third_party_api=TPAPIServiceSP(api_endpoint="http://tp-party-api-endpoint2"))

    def get_profile_name(self):
        return "aws_books_ordering_service"

    def get_book_ordering_service(self):
        return BooksOrderingSystemImpl(books_registry=self.books_registry)


# wire services for GCP cloud provider
class BookOrderingServiceGCPProfile(BookOrderingProfile):

    def __init__(self):
        self.books_registry = BooksOrderingRegistry(
            books_data_store=DataStoreSP(db_connection_str="connection-str-to-db", ssl_cert_path="/your/cert/path3"),
            storage_service=GCPCloudStorageServiceSP(connection_str="gcp-storage-service-connection-string"),
            third_party_api=TPAPIServiceSP(api_endpoint="http://third-party-api-endpoint3"))

    def get_profile_name(self):
        return "gcp_books_ordering_service"

    def get_book_ordering_service(self):
        return BooksOrderingSystemImpl(books_registry=self.books_registry)
