from pathlib import Path

import typer

from instant_python.project_generator.project_generator import ProjectGenerator
from instant_python.question_prompter.basic_prompter import BasicPrompter

app = typer.Typer()


def user_requirements_has_not_been_generated_before() -> bool:
    return Path("user_requirements.yml").exists() is False


@app.command()
def generate_project():
    if user_requirements_has_not_been_generated_before():
        user_requirements = BasicPrompter().ask()
        user_requirements.save_in_memory()

    project_generator = ProjectGenerator()
    project_generator.generate()


if __name__ == "__main__":
    app()
