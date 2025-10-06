from instant_python.config.domain.configuration_schema import ConfigurationSchema
from instant_python.config.domain.dependency_configuration import DependencyConfiguration
from instant_python.config.domain.general_configuration import GeneralConfiguration
from instant_python.config.domain.git_configuration import GitConfiguration
from instant_python.config.domain.template_configuration import TemplateConfiguration
from instant_python.config.domain.yaml_writer import YamlWriter
from instant_python.configuration.questionary_question_wizard import QuestionaryQuestionWizard


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionaryQuestionWizard, writer: YamlWriter) -> None:
        self._question_wizard = question_wizard
        self._writer = writer

    def execute(self) -> None:
        answers = self._question_wizard.run()
        configuration = ConfigurationSchema(
            general=GeneralConfiguration(**answers["general"]),
            dependencies=[DependencyConfiguration(**dependency) for dependency in answers["dependencies"]],
            template=TemplateConfiguration(**answers["template"]),
            git=GitConfiguration(**answers["git"]),
        )
        self._writer.write(configuration)
