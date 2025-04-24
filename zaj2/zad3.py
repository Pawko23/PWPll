from typing import Dict, Optional

class Library:
    def __init__(self, books: Dict[str, str]):
        self.books = books

    def find_book(self, isbn: str) -> Optional[str]:
        return self.books.get(isbn)
    
library = Library({
    "978-83-01-20355-5": "Pan Tadeusz",
    "978-83-240-5736-2": "Lalka"
})

print(library.find_book("978-83-01-20355-5")) 
print(library.find_book("000-00-00000-0"))