from instant_python.builder.jinja_environment import JinjaEnvironment


class ProjectRender:
    def __init__(self, jinja_environment: JinjaEnvironment) -> None:
        self._jinja_environment = jinja_environment