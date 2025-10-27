from jinja2 import Environment


class JinjaEnvironment:
    def __init__(self) -> None:
        self._env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )