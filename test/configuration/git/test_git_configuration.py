from expects import expect, be_true, be_none, be_false, raise_error

from instant_python.configuration.git.git_user_or_email_not_present import (
    GitUserOrEmailNotPresent,
)
from test.configuration.git.git_configuration_mother import GitConfigurationMother


class TestGitConfiguration:
    def test_should_allow_to_initialize_git_with_user_and_email(self) -> None:
        git_configuration = GitConfigurationMother.initialize()

        expect(git_configuration.initialize).to(be_true)
        expect(git_configuration.username).not_to(be_none)
        expect(git_configuration.email).not_to(be_none)

    def test_should_allow_to_not_initialize_git(self) -> None:
        git_configuration = GitConfigurationMother.not_initialize()

        expect(git_configuration.initialize).to(be_false)
        expect(git_configuration.username).to(be_none)
        expect(git_configuration.email).to(be_none)

    def test_should_not_allow_to_initialize_git_if_user_is_not_present(self) -> None:
        expect(lambda: GitConfigurationMother.with_parameters(username=None)).to(raise_error(GitUserOrEmailNotPresent))

    def test_should_not_allow_to_initialize_git_if_email_is_not_present(self) -> None:
        expect(lambda: GitConfigurationMother.with_parameters(email=None)).to(raise_error(GitUserOrEmailNotPresent))
