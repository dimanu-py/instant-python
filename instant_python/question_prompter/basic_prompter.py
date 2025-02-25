import typer
from click import Choice

from instant_python.question_prompter.user_requirements import UserRequirements


class BasicPrompter:

	@classmethod
	def ask(cls) -> UserRequirements:
		project_name = cls._prompt(
			text="Enter the project name", default_value="Project Name"
		)

		default_slug_name = project_name.lower().replace(" ", "-")
		slug = cls._prompt(
			text="Enter the project slug", default_value=default_slug_name
		)

		default_source_name = slug.replace("-", "_")
		source_name = cls._prompt(
			text="Enter the desire name for your source folder",
			default_value=default_source_name,
			options=["src", "source", default_source_name],
		)

		license = cls._prompt(
			text="Select a license",
			default_value="MIT",
			options=["MIT", "Apache", "GPL"],
		)


		version = cls._prompt(
			text="Enter the project initial version", default_value="0.1.0"
		)

		description = cls._prompt(
			text="Enter the project description", default_value="Project Description"
		)

		github_username = cls._prompt(
			text="Enter your github username", default_value="username"
		)

		github_email = cls._prompt(text="Enter your github email")

		python_version = cls._prompt(
			text="Enter the python version",
			default_value="3.13",
			options=["3.13", "3.12", "3.11", "3.10"],
		)

		dependency_manager = cls._prompt(
			text="Select a dependency manager",
			default_value="uv",
			options=["uv", "pdm"],
		)

		python_manager = cls._prompt(
			text="Select a python manager",
			default_value="pyenv",
			options=["pyenv", "uv", "pdm"],
		)

		default_dependencies = cls._confirm(text="Do you want to include default dependencies?")

		template = cls._prompt(
			text="Select your project template",
			default_value="DDD",
			options=["DDD", "Standard"],
		)

		if template == "DDD":
			bounded_context = cls._prompt(
				text="Enter the bounded context name", default_value="Bounded Context"
			)

			aggregate_name = cls._prompt(
				text="Enter the aggregate name", default_value="Aggregate"
			)

			common_ddd_objects = cls._confirm(
				text="Do you want to include common DDD objects?"
			)

			return UserRequirements(
				project_name=project_name,
				slug=slug,
				source_name=source_name,
				license=license,
				version=version,
				description=description,
				github_username=github_username,
				github_email=github_email,
				python_version=python_version,
				dependency_manager=dependency_manager,
				python_manager=python_manager,
				default_dependencies=default_dependencies,
				template=template,
				bounded_context=bounded_context,
				aggregate_name=aggregate_name,
				common_ddd_objects=common_ddd_objects,
			)

		return UserRequirements(
			project_name=project_name,
			slug=slug,
			source_name=source_name,
			license=license,
			version=version,
			description=description,
			github_username=github_username,
			github_email=github_email,
			python_version=python_version,
			dependency_manager=dependency_manager,
			python_manager=python_manager,
			default_dependencies=default_dependencies,
			template=template
		)

	@staticmethod
	def _prompt(
			text: str,
			default_value: str | None = None,
			options: list[str] | None = None,
	) -> str:
		options = Choice(options, case_sensitive=False) if options else None
		show_choices = True if options else False
		return typer.prompt(
			text=text,
			default=default_value,
			type=options,
			show_choices=show_choices,
		)

	@staticmethod
	def _confirm(text: str) -> bool:
		return typer.confirm(text, default=True)
