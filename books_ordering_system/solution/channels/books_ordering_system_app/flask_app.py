"""
Name : flask_app.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 12:40 PM
Desc: flask_app.py
"""
from books_ordering_system.solution.profile.profile_manager import ProfileManager

# your solution code goes here
books_ordering_system_impl = ProfileManager.get_books_ordering_profile().get_book_ordering_service()


# run your logics
books_ordering_system_impl.run_ordering_system()


