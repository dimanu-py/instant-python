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
        self._tree: list[Node] = []
        self._jinja_environment = jinja_environment
        self._project_renderer = JinjaProjectRenderer(jinja_environment=jinja_environment)

    def create_folders_and_files(
        self,
        project_structure: list[dict[str, list[str] | str | bool]],
    ) -> None:
        self._tree = [self._build_node(node) for node in project_structure]

    def _build_node(self, node: dict[str, str | list | bool]) -> Node:
        node_type = node["type"]
        name = node["name"]

        if node_type == NodeType.DIRECTORY:
            children = node.get("children", [])
            is_python_module = node.get("python", False)
            directory_children = [self._build_node(child) for child in children]
            return Directory(name=name, children=directory_children, is_python=is_python_module)
        elif node_type == NodeType.BOILERPLATE:
            extension = node.get("extension", "")
            file = File(name=name, extension=extension)
            self._boilerplate_files.append(file)
            return file
        else:
            raise UnknownNodeTypeError(node_type)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(boilerplate_files={self._boilerplate_files}, tree={self._tree})"