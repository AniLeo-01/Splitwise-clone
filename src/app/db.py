from sqlmodel import SQLModel
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlmodel import SQLModel
from app.config.config import get_settings

DATABASE_URL = get_settings().DB_URL
DATABASE_URL = "postgresql+asyncpg://aniruddha:password@localhost:5432/splitwise"

engine = create_async_engine(
    DATABASE_URL, echo = True
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session= sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session

async def disconnect_db():
    await engine.dispose()