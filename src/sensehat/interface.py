from abc import ABC, abstractmethod


class AbstractSensehatInterface(ABC):
    @abstractmethod
    def fill(self, color: str):
        pass
