from src.question_prompter.boolean_question import BooleanQuestion
from src.question_prompter.choice_question import ChoiceQuestion
from src.question_prompter.free_text_question import FreeTextQuestion
from src.question_prompter.multiple_choice_question import MultipleChoiceQuestion

GENERAL_QUESTIONS = [
    FreeTextQuestion(
        key="project_name",
        message="Enter the name of the project",
        default="Python Project",
    ),
    FreeTextQuestion(
        key="project_slug",
        message="Enter the slug of the project",
        default="python-project",
    ),
    FreeTextQuestion(
        key="source_name", message="Enter the name of the source folder", default="src"
    ),
    FreeTextQuestion(
        key="description",
        message="Enter the project description",
        default="Python Project Description",
    ),
    FreeTextQuestion(
        key="version", message="Enter the project initial version", default="0.1.0"
    ),
    FreeTextQuestion(key="author", message="Enter your name"),
    FreeTextQuestion(key="email", message="Enter your email"),
    ChoiceQuestion(
        key="python_version",
        message="Enter the python version",
        default="3.13",
        options=["3.13", "3.12", "3.11", "3.10"],
    ),
    ChoiceQuestion(
        key="dependency_manager",
        message="Select a dependency manager",
        default="uv",
        options=["uv", "pdm"],
    ),
    ChoiceQuestion(
        key="license",
        message="Select a license",
        default="MIT",
        options=["MIT", "Apache", "GPL"],
    ),
    BooleanQuestion(key="git", message="Do you want to initialize a git repository?"),
    MultipleChoiceQuestion(
        key="built_in_features",
        message="Select the built-in features you want to include (fastapi_application option requires logger)",
        options=[
            "value_objects",
            "github_actions",
            "makefile",
            "synchronous_sqlalchemy",
            "logger",
            "event_bus",
            "async_sqlalchemy",
            "async_alembic",
            "fastapi_application",
        ],
    ),
    BooleanQuestion(
        key="default_dependencies",
        message="Do you want to include default dependencies? (coverage, doublex, doublex-expects, expects, pytest, pytest-watch, pytest-xdist, pytest-sugar, mypy, ruff)",
    ),
    ChoiceQuestion(
        key="template",
        message="Select a template",
        default="domain_driven_design",
        options=["domain_driven_design", "clean_architecture", "empty_project"],
    ),
]

DDD_QUESTIONS = [
    FreeTextQuestion(
        key="bounded_context",
        message="Enter the bounded context name",
        default="backoffice",
    ),
    FreeTextQuestion(
        key="aggregate_name", message="Enter the aggregate name", default="user"
    ),
]
