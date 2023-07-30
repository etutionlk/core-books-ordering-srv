"""
Name : book.py
Author : Chinthaka Maduranga
Contact : etutionlk@gmail.com
Time : 30/07/2023 6:49 AM
Desc: book.py
"""
from typing import Optional

from pydantic import BaseModel, constr


class Book(BaseModel):
    book_name: constr()
    author: constr()
    publisher: constr()
    isbn_no: constr()
    translator: Optional[constr()]
