from dataclasses import dataclass, asdict, field
from datetime import datetime
from pathlib import Path

import yaml


@dataclass
class UserRequirements:
    project_slug: str
    license: str
    version: str
    description: str
    author: str
    python_version: str
    dependency_manager: str
    git: bool = field(default=False)
    source_name: str = field(default_factory=str)
    template: str = field(default_factory=str)
    git_email: str = field(default_factory=str)
    git_user_name: str = field(default_factory=str)
    dependencies: list[str] = field(default_factory=list)
    specify_bounded_context: bool = field(default=False)
    bounded_context: str = field(default_factory=str)
    aggregate_name: str = field(default_factory=str)
    built_in_features: list[str] = field(default_factory=list)
    year: int = field(default=datetime.now().year)

    def __post_init__(self) -> None:
        self._file_path = "user_requirements.yml"

    def to_dict(self) -> dict:
        return asdict(self)

    def save_in_memory(self) -> None:
        with open(self._file_path, "w") as file:
            yaml.dump(self.to_dict(), file)

    def remove(self) -> None:
        Path(self._file_path).unlink()
