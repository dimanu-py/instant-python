import os

from test.configuration.git.git_configuration_mother import GitConfigurationMother
from test.git.mock_git_configurer import MockGitConfigurer


class TestGitConfigurer:
    def setup_method(self) -> None:
        self._git_configurer = MockGitConfigurer(project_directory=os.getcwd())

    def test_should_not_initialize_git_repository_if_is_not_specified(self) -> None:
        configuration = GitConfigurationMother.not_initialize()

        self._git_configurer.setup_repository(configuration=configuration)

        self._git_configurer.expect_to_not_have_initialized_repository()

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
        configuration = GitConfigurationMother.with_parameters(
            username="test_user",
            email="test_email@gmail.com",
        )

        self._git_configurer.setup_repository(configuration=configuration)

        self._git_configurer.expect_to_have_been_called_with(
            "git init",
            "git config user.name test_user",
            "git config user.email test_email@gmail.com",
            "git add .",
            'git commit -m "🎉 chore: initial commit"',
        )
