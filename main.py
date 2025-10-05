from fastapi import FastAPI
from routers.books_get_methods import router as books_router
from routers.books_post_methods import router as post_router


app = FastAPI()

app.include_router(books_router)
app.include_router(post_router)
