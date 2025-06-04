from jinja2 import Environment, PackageLoader


class JinjaEnvironment:
    def __init__(self) -> None:
        self._env = Environment(
	        loader=PackageLoader("instant_python", "templates"),
	        trim_blocks=True,
	        lstrip_blocks=True,
        )
