from sqlalchemy.dialects.postgresql import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.user import TGUserDTO, TGUserCreate
from app.services.abstract.repo import TGUserRepo


class AlchemyTGUserRepo(AlchemyRepo[TGUserDTO], TGUserRepo):
    async def create_if_not_exists(self, tg_user: TGUserCreate) -> None:
        query = (
            insert(self._table)
            .values(tg_user.model_dump())
            .on_conflict_do_nothing(index_elements=("id",))
        )
        return await self.execute(query)
