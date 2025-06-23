import os

from test.configuration.git.git_configuration_mother import GitConfigurationMother
from test.git.mock_git_configurer import MockGitConfigurer


class TestGitConfigurer:
    def test_should_not_initialize_git_repository_if_is_not_specified(self) -> None:
        configuration = GitConfigurationMother.not_initialize()
        git_configurer = MockGitConfigurer(project_directory=os.getcwd())

        git_configurer.setup_repository(configuration=configuration)

        git_configurer.expect_to_not_have_initialized_repository()
