from instant_python.shared.domain.config_schema import ConfigSchema
from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.question_wizard import QuestionWizard


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, writer: ConfigWriter) -> None:
        self._question_wizard = question_wizard
        self._writer = writer

    def execute(self) -> None:
        answers = self._ask_project_configuration_to_user()
        config = ConfigSchema.from_primitives(answers)
        self._save_configuration(config)

    def _save_configuration(self, config: ConfigSchema) -> None:
        self._writer.write(config)

    def _ask_project_configuration_to_user(self) -> dict:
        return self._question_wizard.run()
