from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.configuration_schema import ConfigurationSchema
from instant_python.config.domain.dependency_configuration import DependencyConfiguration
from instant_python.config.domain.general_configuration import GeneralConfiguration
from instant_python.config.domain.git_configuration import GitConfiguration
from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.config.domain.template_configuration import TemplateConfiguration


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, writer: ConfigWriter, parser: ConfigParser) -> None:
        self._question_wizard = question_wizard
        self._writer = writer
        self._parser = parser

    def execute(self) -> None:
        answers = self._question_wizard.run()
        configuration = ConfigurationSchema(
            general=GeneralConfiguration(**answers["general"]),
            dependencies=[DependencyConfiguration(**dependency) for dependency in answers["dependencies"]],
            template=TemplateConfiguration(**answers["template"]),
            git=GitConfiguration(**answers["git"]),
        )
        self._writer.write(configuration)
