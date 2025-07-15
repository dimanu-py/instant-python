from jinja2 import Environment, PackageLoader

from instant_python.render.jinja_custom_filters import is_in, compute_base_path, has_dependency


class JinjaEnvironment:
    def __init__(self, package_name: str, template_directory: str) -> None:
        self._env = Environment(
            loader=PackageLoader(package_name, template_directory),
            trim_blocks=True,
            lstrip_blocks=True,
            autoescape=True,
        )
        self._env.filters["is_in"] = is_in
        self._env.filters["compute_base_path"] = compute_base_path
        self._env.filters["has_dependency"] = has_dependency

    def render_template(self, name: str, context: dict[str, str] = None) -> str:
        """Renders a template with the given context.

        Args:
            name: The name of the template to render
            context: A dictionary of variables to pass to the template

        Returns:
            The rendered template as a string
        """
        template = self._env.get_template(name)
        return template.render(**(context or {}))
