import random
from typing import List, Dict

class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_books_by_author(self, author: str) -> List[Book]:
        return [book for book in self.books if book.author.lower() == author.lower()]

    def get_random_book(self) -> Book:
        return random.choice(self.books) if self.books else None

    def get_book_stats(self) -> Dict[str, int]:
        years = [book.year for book in self.books]
        return {
            "total_books": len(self.books),
            "oldest_book": min(years) if years else None,
            "newest_book": max(years) if years else None
        }

# Example usage
library = Library()
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))

print(f"Library stats: {library.get_book_stats()}")

author = "George Orwell"
books_by_author = library.find_books_by_author(author)
print(f"Books by {author}: {[book.title for book in books_by_author]}")

random_book = library.get_random_book()
if random_book:
    print(f"Random book: {random_book.title} ({random_book.year})")