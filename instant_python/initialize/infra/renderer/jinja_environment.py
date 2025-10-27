from collections.abc import Callable

from jinja2 import Environment


class JinjaEnvironment:
    def __init__(self) -> None:
        self._env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )

    def add_filter(self, name: str, filter_: Callable) -> None:
        self._env.filters[name] = filter_
