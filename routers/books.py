from fastapi import APIRouter

router = APIRouter()

# Simple test endpoint
@router.get("/test")
async def read_root():
    return {"Hello": "World"}


books = [
    {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian",
        "isbn": "9780451524935"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Fiction",
        "isbn": "9780061120084"
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Classic",
        "isbn": "9780743273565"
    },
    {
        "id": 4,
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945,
        "genre": "Dystopian",
        "isbn": "9780451526342"
    },
    {
        "id": 5,
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genre": "Dystopian",
        "isbn": "9780060850524"
    },
    {
        "id": 6,
        "title": "Brave New World",
        "author": "Shane Clark",
        "year": 2025,
        "genre": "History",
        "isbn": "9789990850524"
    },
    {
        "id": 7,
        "title": "Go Set a Watchman",
        "author": "Harper Lee",
        "year": 2015,
        "genre": "Fiction",
        "isbn": "9780062409850"
    }
]



# Endpoint to get all books
@router.get("/books/")
async def read_books():
    return books


# Endpoint to get a book by its ID
@router.get("/books/{book_id}")
async def read_book(book_id: int):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return book
    return {"error": "Book not found"}





