from doublex import Mock

from instant_python.config.domain.yaml_writer import YamlWriter
from instant_python.configuration.question_wizard import QuestionWizard
from instant_python.config.application.config_generator import ConfigGenerator
from test.config.domain.mothers.configuration_schema_mother import ConfigurationSchemaMother


class TestConfigGenerator:
    def test_should_generate_configuration(self) -> None:
        question_wizard = Mock(QuestionWizard)
        configuration_writer = Mock(YamlWriter)
        config_generator = ConfigGenerator(
            question_wizard=question_wizard,
            writer=configuration_writer,
        )
        configuration = ConfigurationSchemaMother.any()

        config_generator.execute()

        self._should_have_called_question_wizard(configuration)
        self._should_have_called_configuration_writer(configuration)
