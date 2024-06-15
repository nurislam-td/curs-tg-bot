from sqlalchemy.dialects.postgresql import insert

from app.adapters.base_repo import AlchemyRepo
from app.services.entity.chat import ChatDTO, ChatCreate
from app.services.abstract.repo import ChatRepo


class AlchemyChatRepo(AlchemyRepo[ChatDTO], ChatRepo):
    async def create_if_not_exists(self, chat: ChatCreate) -> None:
        query = (
            insert(self._table)
            .values(chat.model_dump())
            .on_conflict_do_nothing(index_elements=("id",))
        )
        return await self.execute(query)
