from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Query

from database import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session


def pagination_params(
    skip: int = Query(0,ge=0,),
    limit: int = Query(10, ge=1, le=100),
):
    return {"skip": skip, "limit": limit}
