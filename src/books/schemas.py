from pydantic import BaseModel


class Books(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str




class BookUpdate(BaseModel):
    title: str
    author: str
    page_count: int
    language: str



