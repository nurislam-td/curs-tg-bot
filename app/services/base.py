import dataclasses


@dataclasses.dataclass
class Base:
    def as_dict(self):
        return dataclasses.asdict(self)
