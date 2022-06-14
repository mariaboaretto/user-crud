from abc import ABC, abstractmethod
from flask import Flask


class ControllerInterface(ABC):

    @abstractmethod
    def set_endpoints(self, app: Flask) -> None:
        pass