from abc import ABC, abstractmethod


class QuestionWizard(ABC):
    @abstractmethod
    def run(self) -> dict:
        raise NotImplementedError
