from abc import ABC, abstractmethod


class TemplateManager(ABC):
    @abstractmethod
    def get_project(self, template_name: str) -> dict:
        raise NotImplementedError
