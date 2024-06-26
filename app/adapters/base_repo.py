from typing import Type, TypeVar, cast, override
from uuid import UUID

from sqlalchemy import (
    Delete,
    Insert,
    Result,
    Select,
    TableClause,
    Update,
    delete,
    insert,
    select,
    update,
)
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.services.abstract.repo import DTO, Repo

DBModel = TypeVar("DBModel", bound=DeclarativeBase)


class AlchemyRepo(Repo[DTO]):
    def __init__(
        self,
        session: AsyncSession,
        schema: Type[DTO],
        model: Type[DBModel],
    ) -> None:
        self.session = session
        self._schema = schema
        self._model = model
        self._table = cast(TableClause, model.__table__)
        self._pk_col = model.__table__.primary_key.columns[0]

    async def fetch_one(self, query: Select | Insert | Update) -> DTO | None:
        result: Result = await self.session.execute(query)
        data = result.mappings().one_or_none()
        return self._schema(**data) if data else None

    async def fetch_all(self, query: Select | Insert | Update) -> list[DTO] | None:
        result: Result = await self.session.execute(query)
        data_list = result.mappings().all()
        return [self._schema(**data) for data in data_list] if data_list else None

    async def execute(self, query: Insert | Update | Delete) -> None:
        await self.session.execute(query)

    @override
    async def create(self, values: dict) -> DTO | None:
        query = insert(self._table).values(**values).returning(self._model)
        return await self.fetch_one(query)

    @override
    async def get_all(self, **kwargs) -> list[DTO] | None:
        query = select(self._table).filter_by(**kwargs)
        return await self.fetch_all(query)

    @override
    async def get(self, pk):
        query = select(self._table).where(self._pk_col == pk)
        return await self.fetch_one(query)

    @override
    async def update(self, values: dict, filters: dict) -> list[DTO] | None:
        query = (
            update(self._table)
            .values(**values)
            .filter_by(**filters)
            .returning(self._model)
        )
        return await self.fetch_all(query)

    @override
    async def update_one(self, values: dict, pk: UUID | int) -> DTO | None:
        query = (
            update(self._table)
            .where(self._pk_col == pk)
            .values(**values)
            .returning(self._model)
        )
        return await self.fetch_one(query)

    @override
    async def delete(self, filters: dict) -> None:
        query = delete(self._table).filter_by(**filters)
        return await self.execute(query)
