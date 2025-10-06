from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.config.domain.yaml_writer import YamlWriter
from instant_python.configuration.questionary_question_wizard import QuestionaryQuestionWizard
from instant_python.config.application.config_generator import ConfigGenerator
from test.config.domain.mothers.configuration_schema_mother import ConfigurationSchemaMother


class TestConfigGenerator:
    def test_should_generate_configuration(self) -> None:
        question_wizard = Mock(QuestionaryQuestionWizard)
        configuration_writer = Mock(YamlWriter)
        config_generator = ConfigGenerator(
            question_wizard=question_wizard,
            writer=configuration_writer,
        )
        configuration = ConfigurationSchemaMother.any()

        expect_call(question_wizard).run().returns(configuration.to_primitives())
        expect_call(configuration_writer).write(configuration)

        config_generator.execute()

        expect(question_wizard).to(have_been_satisfied)
        expect(configuration_writer).to(have_been_satisfied)