from jinja2 import Environment, PackageLoader

from instant_python.project_generator.jinja_custom_filters import is_in, compute_base_path


class JinjaEnvironment:
    def __init__(self, package_name: str, template_directory: str) -> None:
        self._env = Environment(
	        loader=PackageLoader(package_name, template_directory),
	        trim_blocks=True,
	        lstrip_blocks=True,
        )
        self._env.filters["is_in"] = is_in
        self._env.filters["compute_base_path"] = compute_base_path
