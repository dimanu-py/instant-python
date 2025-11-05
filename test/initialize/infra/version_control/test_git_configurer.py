import os

from doublex import Mock, Mimic, expect_call
from doublex_expects import have_been_satisfied
from expects import expect

from instant_python.initialize.infra.env_manager.system_console import SystemConsole
from instant_python.initialize.infra.version_control.git_configurer import GitConfigurer
from test.config.domain.mothers.git_config_mother import GitConfigMother
from test.initialize.infra.env_manager.mother.command_execution_result_mother import CommandExecutionResultMother
from test.initialize.infra.version_control.mock_git_configurer import MockGitConfigurer


class TestGitConfigurer:
    _SUCCESSFUL_COMMAND_RESULT = CommandExecutionResultMother.success()
    _FAILED_COMMAND_RESULT = CommandExecutionResultMother.failure()
    _A_USERNAME = "test_user"
    _A_EMAIL = "test_user@gmail.com"

    def setup_method(self) -> None:
        self._console = Mimic(Mock, SystemConsole)
        self._git_configurer = MockGitConfigurer(project_directory=os.getcwd())

    def test_should_configure_git_repository_successfully(self) -> None:
        configurer = GitConfigurer(project_directory=os.getcwd(), console=self._console)

        self._should_create_repository()
        self._should_set_user_information()
        self._should_make_first_commit()

        configurer.setup(GitConfigMother.with_parameters(
            username=self._A_USERNAME,
            email=self._A_EMAIL,
        ))

        expect(self._console).to(have_been_satisfied)

    def test_should_initialize_git_repository(self) -> None:
        self._git_configurer._initialize_repository()

        self._git_configurer.expect_to_have_been_called_with("git init")

    def test_should_set_username_and_email_when_initializing_repository(self) -> None:
        self._git_configurer._set_user_information(username="test_user", email="test.user@gmail.com")

        self._git_configurer.expect_to_have_been_called_with(
            "git config user.name test_user",
            "git config user.email test.user@gmail.com",
        )

    def test_should_make_initial_commit_after_initializing_repository(self) -> None:
        self._git_configurer._make_initial_commit()

        self._git_configurer.expect_to_have_been_called_with(
            "git add .",
            'git commit -m "🎉 chore: initial commit"',
        )

    def test_should_setup_git_repository(self) -> None:
        configuration = GitConfigMother.with_parameters(
            username="test_user",
            email="test_email@gmail.com",
        )

        self._git_configurer.setup(config=configuration)

        self._git_configurer.expect_to_have_been_called_with(
            "git init",
            "git config user.name test_user",
            "git config user.email test_email@gmail.com",
            "git add .",
            'git commit -m "🎉 chore: initial commit"',
        )

    def _should_create_repository(self) -> None:
        expect_call(self._console).execute("git init").returns(self._SUCCESSFUL_COMMAND_RESULT)

    def _should_set_user_information(self) -> None:
        expect_call(self._console).execute(f"git config user.name {self._A_USERNAME}").returns(self._SUCCESSFUL_COMMAND_RESULT)
        expect_call(self._console).execute(f"git config user.email {self._A_EMAIL}").returns(self._SUCCESSFUL_COMMAND_RESULT)

    def _should_make_first_commit(self) -> None:
        expect_call(self._console).execute("git add .").returns(self._SUCCESSFUL_COMMAND_RESULT)
        expect_call(self._console).execute('git commit -m "🎉 chore: initial commit"').returns(self._SUCCESSFUL_COMMAND_RESULT)
