from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

@app.get("/test")
async def read_root():
    return {"Hello": "World"}


books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "genre": "Dystopian",
        "isbn": "9780451524935"
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,
        "genre": "Fiction",
        "isbn": "9780061120084"
    },
    {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": 1925,
        "genre": "Classic",
        "isbn": "9780743273565"
    },
    {
        "title": "Animal Farm",
        "author": "George Orwell",
        "year": 1945,
        "genre": "Dystopian",
        "isbn": "9780451526342"
    },
    {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "year": 1932,
        "genre": "Dystopian",
        "isbn": "9780060850524"
    },
        {
        "title": "Brave New World",
        "author": "Shane Clark",
        "year": 2025,
        "genre": "History",
        "isbn": "9789990850524"
    },
    {
        "title": "Go Set a Watchman",
        "author": "Harper Lee",
        "year": 2015,
        "genre": "Fiction",
        "isbn": "9780062409850"
    }
]


    
