from dataclasses import dataclass, field, asdict


@dataclass
class DependencyConfiguration:
    name: str
    version: str
    is_dev: bool = field(default=False)
    group: str = field(default_factory=str)

    def to_primitives(self) -> dict[str, str | bool]:
        return asdict(self)
