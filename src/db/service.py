from typing import List

from sqlalchemy import select

from db.base import db


class ModelService:

    MODEL = None

    @classmethod
    async def create(cls, data: dict):
        async with db.async_session() as session:
            session.add(cls.MODEL(**data))
            await session.commit()

    @classmethod
    async def get_all(cls) -> List[MODEL]:
        async with db.async_session() as session:
            result = await session.execute(select(cls.MODEL))
            return result.scalars().all()

    @classmethod
    async def get_by_id(cls, object_id: int) -> MODEL:
        async with db.async_session() as session:
            result = await session.execute(select(cls.MODEL).where(cls.MODEL.id == object_id))
            return result.scalars().first()

    @classmethod
    async def update_from_dict(cls, data: dict) -> None:
        ...

    @classmethod
    async def delete_by_id(cls, object_id: int) -> None:
        ...
