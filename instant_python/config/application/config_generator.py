from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_schema import ConfigSchema
from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.question_wizard import QuestionWizard


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, writer: ConfigWriter, parser: ConfigParser) -> None:
        self._question_wizard = question_wizard
        self._writer = writer
        self._parser = parser

    def execute(self) -> None:
        answers = self._ask_project_configuration_to_user()
        config = self._validate_project_configuration(answers)
        self._save_configuration(config)

    def _save_configuration(self, config: ConfigSchema) -> None:
        self._writer.write(config)

    def _validate_project_configuration(self, answers: dict) -> ConfigSchema:
        return self._parser.parse(answers)

    def _ask_project_configuration_to_user(self) -> dict:
        return self._question_wizard.run()
