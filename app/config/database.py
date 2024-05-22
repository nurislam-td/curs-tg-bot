from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config.settings import settings

if settings.mode == "DEV":
    DATABASE_URL = settings.db_url
    DATABASE_PARAMS = {}
else:
    DATABASE_URL = "test url"
    DATABASE_PARAMS = {"poolclass": NullPool}

async_engine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(
    async_engine, autoflush=False, expire_on_commit=False
)
