from collections.abc import Callable

from jinja2 import Environment

from instant_python.render.unknown_template_error import UnknownTemplateError
from instant_python.shared.supported_templates import SupportedTemplates


class JinjaEnvironment:
    def __init__(self, user_template_path: str) -> None:
        self._env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )
        self.add_filter("is_in", _is_in)
        self.add_filter("compute_base_path", _compute_base_path)
        self.add_filter("has_dependency", _has_dependency)

    def add_filter(self, name: str, filter_: Callable) -> None:
        self._env.filters[name] = filter_


def _is_in(values: list[str], container: list) -> bool:
    return any(value in container for value in values)


def _has_dependency(dependencies: list[dict], dependency_name: str) -> bool:
    return any(dep.get("name") == dependency_name for dep in dependencies)


def _compute_base_path(initial_path: str, template_type: str) -> str:
    if template_type == SupportedTemplates.DDD:
        return initial_path

    path_components = initial_path.split(".")
    if template_type == SupportedTemplates.CLEAN:
        return ".".join(path_components[1:])
    elif template_type == SupportedTemplates.STANDARD:
        return ".".join(path_components[2:])
    else:
        raise UnknownTemplateError(template_type)
