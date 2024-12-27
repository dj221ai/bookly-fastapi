from fastapi import status, APIRouter
from fastapi.exceptions import HTTPException
from typing import List
from src.books.schemas import Books, BookUpdate


book_router = APIRouter()



@book_router.get("/", response_model=List[Books], status_code=status.HTTP_200_OK)
async def get_all_books():
    pass


@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Books) -> dict:
    pass


# @book_router.get('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
@book_router.get('/{book_id}')
async def get_a_book(book_id: int) -> dict:
    pass


@book_router.patch('/{book_id}')
async def update_a_book(book_id: int, book_update: BookUpdate) -> dict:
    pass


@book_router.delete('/{book_id}')
# @book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int) -> dict:
    pass
