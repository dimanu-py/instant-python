from typing import Union

from instant_python.configuration.question.boolean_question import BooleanQuestion
from instant_python.configuration.question.conditional_question import ConditionalQuestion
from instant_python.configuration.question.free_text_question import FreeTextQuestion
from instant_python.configuration.question.questionary import Questionary
from instant_python.configuration.step.steps import Step


class DependenciesStep(Step):
    def __init__(self, questionary: Questionary) -> None:
        super().__init__(questionary)

    def run(self) -> dict[str, list[dict[str, Union[str, bool]]]]:
        dependencies = []
        while True:
            user_wants_to_install_dependencies = BooleanQuestion(
                key="keep_asking",
                message="Do you want to install dependencies?",
                default=False,
                questionary=self._questionary,
            ).ask()["keep_asking"]

            if not user_wants_to_install_dependencies:
                break

            dependency_name = FreeTextQuestion(
                key="name",
                message="Enter the name of the dependency you want to install",
                questionary=self._questionary,
            ).ask()

            if not dependency_name["name"]:
                print("Dependency name cannot be empty. Let's try again.")
                continue

            version = FreeTextQuestion(
                key="version",
                message="Enter the version of the dependency",
                default="latest",
                questionary=self._questionary,
            ).ask()

            is_dev_and_belongs_to_group = ConditionalQuestion(
                base_question=BooleanQuestion(
                    key="is_dev",
                    message=f"Do you want to install {dependency_name['name']} as a dev dependency?",
                    default=False,
                    questionary=self._questionary,
                ),
                subquestions=[
                    FreeTextQuestion(
                        key="group",
                        message="Specify the name of the group where to install the dependency (leave empty if not applicable)",
                        default="",
                        questionary=self._questionary,
                    )
                ],
                condition=True,
            ).ask()

            dependencies.append(
                {
                    **dependency_name,
                    **version,
                    **is_dev_and_belongs_to_group,
                }
            )

        return {"dependencies": dependencies}
