
from fastapi import Body,APIRouter
import routers.books_get_methods

router = APIRouter()

book_list = routers.books_get_methods.books

# Simple test endpoint
# Delete is the method used to remove existing resources on the server
# Data is typically sent in the request body in formats like JSON
# Example: Deleting an existing book entry
@router.delete("/books/delete_book/{book_id}")
async def delete_book(book_id: int):
    for idx, b in enumerate(book_list):
        if b.get("id") == book_id:
            book_list.remove(b)
            print(book_list)
            return {"message": "Book deleted successfully"}
    return {"message": "Book not found"}
    
    
        