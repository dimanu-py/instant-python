from dataclasses import dataclass, field


@dataclass(frozen=True)
class Question:
	key: str
	message: str
	default: str = field(default_factory=str)
	options: list[str] = field(default_factory=list)
	confirm: bool = field(default=False)
