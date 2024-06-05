from app.adapters.base_repo import AlchemyRepo
from app.services.entity.keyword import KeywordGroup
from app.services.abstract.repo import KeywordGroupRepo


class AlchemyKeywordGroupRepo(AlchemyRepo[KeywordGroup], KeywordGroupRepo):
    pass
