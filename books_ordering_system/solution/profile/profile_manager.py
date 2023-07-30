"""
Name : profile_manager.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 28/07/2023 8:03 PM
Desc: profile_manager.py
"""
import os

from books_ordering_system.core.books_ordering_system.spi.books_ordering_service.exceptions import NoProfileFoundError
from books_ordering_system.solution.profile.books_ordering_profile import BookOrderingServiceAzureProfile, \
    BookOrderingServiceAWSProfile, BookOrderingServiceGCPProfile

# define cloud provider
cloud_provider = os.environ.get("CLOUD_SERVICE_PROVIDER", "gcp")


class ProfileManager:

    @staticmethod
    def get_books_ordering_profile():
        cloud = cloud_provider.lower()

        if cloud == "azure":
            return BookOrderingServiceAzureProfile()
        elif cloud == "aws":
            return BookOrderingServiceAWSProfile()
        elif cloud == "gcp":
            return BookOrderingServiceGCPProfile()
        else:
            raise NotImplementedError("No such Profile found for cloud provider : {}".format(cloud_provider))

