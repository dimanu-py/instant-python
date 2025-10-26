from doublex import Mock, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.config.application.config_generator import ConfigGenerator
from instant_python.config.domain.config_parser import ConfigParser
from instant_python.config.domain.question_wizard import QuestionWizard
from instant_python.config.domain.config_writer import ConfigWriter
from test.config.domain.mothers.config_schema_mother import ConfigSchemaMother


class TestConfigGenerator:
    def test_should_generate_config(self) -> None:
        question_wizard = Mock(QuestionWizard)
        config_writer = Mock(ConfigWriter)
        config_parser = Mock(ConfigParser)
        config_generator = ConfigGenerator(
            question_wizard=question_wizard,
            writer=config_writer,
            parser=config_parser,
        )
        config = ConfigSchemaMother.any()

        expect_call(question_wizard).run().returns(config.to_primitives())
        expect_call(config_parser).parse(config.to_primitives()).returns(config)
        expect_call(config_writer).write(config)

        config_generator.execute()

        expect(question_wizard).to(have_been_satisfied)
        expect(config_parser).to(have_been_satisfied)
        expect(config_writer).to(have_been_satisfied)
