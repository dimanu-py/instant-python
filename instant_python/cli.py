import typer

from instant_python.project_generator.project_generator import ProjectGenerator
from instant_python.question_prompter.basic_prompter import BasicPrompter

app = typer.Typer()


@app.command()
def generate_project():
    user_requirements = BasicPrompter().ask()
    user_requirements.save_in_memory()

    project_generator = ProjectGenerator()
    project_generator.generate()


if __name__ == "__main__":
    app()
