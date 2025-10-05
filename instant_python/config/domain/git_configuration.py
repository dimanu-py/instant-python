from dataclasses import dataclass, field, asdict
from typing import Optional

from instant_python.shared.application_error import ApplicationError
from instant_python.shared.error_types import ErrorTypes


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


class GitUserOrEmailNotPresent(ApplicationError):
    def __init__(self) -> None:
        message = "When initializing a git repository, both username and email must be provided."
        super().__init__(message=message, error_type=ErrorTypes.CONFIGURATION.value)
