from abc import ABC, abstractmethod
from core.user import User


class UserPersistenceInterface(ABC):
    # Reads from file and loads data into user array
    @abstractmethod
    def load_data(self) -> list[User]:
        pass

    # Writes data from user_list into a file
    @abstractmethod
    def persist_data(self, user_list: list):
        pass

