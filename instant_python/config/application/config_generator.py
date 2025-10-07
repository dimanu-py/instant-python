from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.config_writer import ConfigWriter
from instant_python.config.domain.question_wizard import QuestionWizard


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, writer: ConfigWriter, parser: ConfigParser) -> None:
        self._question_wizard = question_wizard
        self._writer = writer
        self._parser = parser

    def execute(self) -> None:
        answers = self._question_wizard.run()
        configuration = self._parser.parse(answers)
        self._writer.write(configuration)
