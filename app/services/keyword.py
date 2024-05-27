import dataclasses
from datetime import datetime

from app.services.abstract.unit_of_work import UnitOfWork


@dataclasses.dataclass(frozen=True)
class KeywordGroup:
    id: int
    title: str
    description: str
    keywords: list[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    def as_dict(self):
        return dataclasses.asdict(self)


async def create_keyword_group(
    keyword_group: KeywordGroup, uow: UnitOfWork
) -> KeywordGroup:
    async with uow:
        created = await uow.keyword_group.create(values=keyword_group.as_dict())
        await uow.commit()
        return created
