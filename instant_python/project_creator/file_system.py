from pathlib import Path

from instant_python.configuration.configuration_schema import ConfigurationSchema
from instant_python.errors.unknown_node_typer_error import UnknownNodeTypeError
from instant_python.project_creator.directory import Directory
from instant_python.project_creator.file import File
from instant_python.project_creator.node import Node, NodeType
from instant_python.render.jinja_environment import JinjaEnvironment
from instant_python.render.jinja_project_renderer import JinjaProjectRenderer


class FileSystem:
    def __init__(self, jinja_environment: JinjaEnvironment) -> None:
        self._boilerplate_files: list[File] = []
        self._jinja_environment = jinja_environment
        self._project_renderer = JinjaProjectRenderer(jinja_environment=jinja_environment)

    def create_folders_and_files(self, context_config: ConfigurationSchema, template_base_dir: str) -> None:
        project_structure = self._project_renderer.render_project_structure(
            context_config=context_config,
            template_base_dir=template_base_dir,
        )
        tree = [self._build_tree(node) for node in project_structure]
        for node in tree:
            node.create(base_path=Path(context_config.project_folder_name))

    def _build_tree(self, node: dict[str, str | list | bool]) -> Node:
        node_type = node["type"]
        name = node["name"]

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [self._build_tree(child) for child in children]
            return Directory(name=name, children=directory_children, is_python=is_python_module)
        elif node_type == NodeType.BOILERPLATE:
            extension = node.get("extension", "")
            file = File(name=name, extension=extension)
            self._boilerplate_files.append(file)
            return file
        else:
            raise UnknownNodeTypeError(node_type)
