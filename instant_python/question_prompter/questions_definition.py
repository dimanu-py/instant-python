from instant_python.question_prompter.question import Question

GENERAL_QUESTIONS = [
    Question(
        key="project_name",
        message="Enter the name of the project",
        default="Python Project",
    ),
    Question(
        key="project_slug",
        message="Enter the slug of the project",
        default="python_project",
    ),
    Question(
        key="source_name", message="Enter the name of the source folder", default="src"
    ),
    Question(
        key="description",
        message="Enter the project description",
        default="Python Project Description",
    ),
    Question(
        key="version", message="Enter the project initial version", default="0.1.0"
    ),
    Question(key="github_username", message="Enter your github username"),
    Question(key="github_email", message="Enter your github email"),
    Question(
        key="python_version",
        message="Enter the python version",
        default="3.13",
        options=["3.13", "3.12", "3.11", "3.10"],
    ),
    Question(
        key="dependency_manager",
        message="Select a dependency manager",
        default="uv",
        options=["uv", "pdm"],
    ),
    Question(
        key="python_manager",
        message="Select a python manager",
        default="uv",
        options=["pyenv", "uv", "pdm"],
    ),
    Question(
        key="license",
        message="Select a license",
        default="MIT",
        options=["MIT", "Apache", "GPL"],
    ),
    Question(
        key="git", message="Do you want to initialize a git repository?", confirm=True
    ),
    Question(
        key="built_in_features",
        message="Select the built-in features you want to include",
        multiselect=True,
        options=["Value Objects", "Github Actions", "Makefile", "Pre commit"],
    ),
    Question(
        key="template",
        message="Select a template",
        default="Domain Driven Design",
        options=["Domain Driven Design", "Clean Architecture", "Empty Project"],
    ),
]

DDD_QUESTIONS = [
    Question(
        key="bounded_context",
        message="Enter the bounded context name",
        default="backoffice",
    ),
    Question(key="aggregate_name", message="Enter the aggregate name", default="user"),
    Question(
        key="default_dependencies",
        message="Do you want to include default dependencies?",
        confirm=True,
    ),
]
