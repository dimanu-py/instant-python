from instant_python.config.domain.yaml_writer import YamlWriter
from instant_python.configuration.question_wizard import QuestionWizard


class ConfigGenerator:
    def __init__(self, question_wizard: QuestionWizard, writer: YamlWriter) -> None:
        self._question_wizard = question_wizard
        self._writer = writer
