import dataclasses


@dataclasses.dataclass
class Base[T]:
    def as_dict(self):
        return dataclasses.asdict(self)
