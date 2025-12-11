from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass(frozen=True)
class UsageMetricsData:
    ipy_version: str
    operating_system: str
    python_version: str
    command: str
    template: str
    built_in_features: list[str] = field(default_factory=list)

    def to_primitives(self) -> dict[str, str]:
        return asdict(self)
