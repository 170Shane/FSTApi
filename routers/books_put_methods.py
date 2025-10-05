
from fastapi import Body,APIRouter
import routers.books_get_methods

router = APIRouter()

book_list = routers.books_get_methods.books

# Simple test endpoint
# Put is the method used to update existing resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Updating an existing book entry
@router.put("/books/update_book/{book_id}")
async def update_book(book_id: int, book: dict = Body()):
    for idx, b in enumerate(book_list):
        if b.get("id") == book_id:
            book_list[idx] = book
            print(book_list)
            return {"message": "Book updated successfully", "book": book}    
    return {"message": "Book not found"}
    
    
        