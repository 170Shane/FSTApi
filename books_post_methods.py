from fastapi import Body,APIRouter
import routers.books_get_methods

router = APIRouter()

book_list = routers.books_get_methods.books

# Simple test endpoint
# Post is the method used to create new resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Creating a new book entry
@router.post("/books/create_book")
async def create_book(book: dict = Body()):
    book_list.append(book)
    print(book_list)
    return {"message": "Book created successfully", "book": book_list}
        