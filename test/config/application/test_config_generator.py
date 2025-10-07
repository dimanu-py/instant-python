from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.config.application.config_generator import ConfigGenerator
from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.config.domain.config_writer import ConfigWriter
from test.config.domain.mothers.configuration_schema_mother import ConfigurationSchemaMother


class TestConfigGenerator:
    def test_should_generate_configuration(self) -> None:
        question_wizard = Mock(QuestionWizard)
        configuration_writer = Mock(ConfigWriter)
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
