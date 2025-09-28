from fastapi import APIRouter
import routers.books_get_methods

router = APIRouter()

# Simple test endpoint
# Post is the method used to create new resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Creating a new book entry
@router.post("/create_book")
async def create_book(book: dict):
    routers.books_get_methods.books.append(book)
    print(routers.books_get_methods.books)
    return {"message": "Book created successfully", "book": routers.books_get_methods.books}
        