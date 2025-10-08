from typing import Union

from instant_python.config.infra.question_wizard.question.boolean_question import BooleanQuestion
from instant_python.config.infra.question_wizard.question.conditional_question import ConditionalQuestion
from instant_python.config.infra.question_wizard.question.free_text_question import FreeTextQuestion
from instant_python.config.infra.question_wizard.question.questionary import Questionary
from instant_python.config.infra.question_wizard.step.steps import Step


class DependenciesStep(Step):
    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)

    def run(self) -> dict[str, list[dict[str, Union[str, bool]]]]:
        dependencies = []
        while True:
            user_wants_to_install_dependencies = self._questionary.boolean_question(
                message="Do you want to install dependencies?",
            )

            if not user_wants_to_install_dependencies:
                break

            name = self._questionary.free_text_question(
                message="Enter the name of the dependency you want to install",
            )

            if not name:
                print("Dependency name cannot be empty. Let's try again.")
                continue

            version = self._questionary.free_text_question(
                message="Enter the version of the dependency you want to install",
                default="latest",
            )

            is_for_development = self._questionary.boolean_question(
                message=f"Do you want to install {name} as a dev dependency?",
                default=False,
            )

            group_name = ""
            if is_for_development:
                group_name = self._questionary.free_text_question(
                    message="Specify the name of the group where to install the dependency (leave empty if not applicable)",
                    default="",
                )

            dependencies.append(
                {
                    "name": name,
                    "version": version,
                    "is_dev": is_for_development,
                    "group": group_name,
                }
            )

        return {"dependencies": dependencies}
