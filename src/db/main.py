from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config

# load_dotenv()

# tmpPostgres = urlparse(os.getenv("DATABASE_URL"))

# async def async_main() -> None:
#     engine = create_async_engine(f"postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require", echo=True)
#     async with engine.connect() as conn:
#         result = await conn.execute(text("select 'hello world'"))
#         print(result.fetchall())
#     await engine.dispose()

# asyncio.run(async_main())


engine = AsyncEngine(
    create_engine(
    url=Config.DATABASE_URL,
    echo=True   
)
)



async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)
        