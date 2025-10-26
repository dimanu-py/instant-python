from typing import Union

import pytest
from expects import expect, be_true, be_none, be_false, raise_error

from instant_python.config.domain.git_config import GitUserOrEmailNotPresent
from test.config.domain.mothers.git_config_mother import GitConfigMother


class TestGitConfig:
    def test_should_allow_to_initialize_git_with_user_and_email(self) -> None:
        git_config = GitConfigMother.initialize()

        expect(git_config.initialize).to(be_true)
        expect(git_config.username).not_to(be_none)
        expect(git_config.email).not_to(be_none)

    def test_should_allow_to_not_initialize_git(self) -> None:
        git_config = GitConfigMother.not_initialize()

        expect(git_config.initialize).to(be_false)
        expect(git_config.username).to(be_none)
        expect(git_config.email).to(be_none)

    @pytest.mark.parametrize(
        "username",
        [
            pytest.param(None, id="username is None"),
            pytest.param("", id="username is empty"),
        ],
    )
    def test_should_not_allow_to_initialize_git_if_user_is_not_present(self, username: Union[str, None]) -> None:
        expect(lambda: GitConfigMother.with_parameters(username=username)).to(
            raise_error(GitUserOrEmailNotPresent)
        )

    @pytest.mark.parametrize(
        "email",
        [
            pytest.param(None, id="email is None"),
            pytest.param("", id="email is empty"),
        ],
    )
    def test_should_not_allow_to_initialize_git_if_email_is_not_present(self, email: Union[str, None]) -> None:
        expect(lambda: GitConfigMother.with_parameters(email=None)).to(raise_error(GitUserOrEmailNotPresent))
