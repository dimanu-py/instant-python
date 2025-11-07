from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.config.application.config_generator import ConfigGenerator
from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.config.domain.config_writer import ConfigWriter
from test.shared.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestConfigGenerator:
    def test_should_generate_config(self) -> None:
        question_wizard = Mock(QuestionWizard)
        config_writer = Mock(ConfigWriter)
        config_generator = ConfigGenerator(question_wizard=question_wizard, writer=config_writer)
        config = ConfigSchemaMother.any()

        expect_call(question_wizard).run().returns(config.to_primitives())
        expect_call(config_writer).write(config)

        config_generator.execute()

        expect(question_wizard).to(have_been_satisfied)
        expect(config_writer).to(have_been_satisfied)
