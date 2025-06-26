from dataclasses import dataclass, field, asdict
from typing import Optional

from instant_python.configuration.git.git_user_or_email_not_present import (
    GitUserOrEmailNotPresent,
)


@dataclass
class GitConfiguration:
    initialize: bool
    username: Optional[str] = field(default=None)
    email: Optional[str] = field(default=None)

    def __post_init__(self) -> None:
        self._ensure_username_and_email_are_set_if_initializing()

    def _ensure_username_and_email_are_set_if_initializing(self) -> None:
        if self.initialize and (self.username is None or self.email is None):
            raise GitUserOrEmailNotPresent()

    def to_primitives(self) -> dict[str, str | bool]:
        return asdict(self)
