from core.user_persistence_interface import UserPersistenceInterface
from core.user import User
import jsonpickle


class UserPersistenceJson(UserPersistenceInterface):
    def load_data(self) -> list[User]:
        with open("user_list.json", "r") as f:
            user_list = jsonpickle.decode(f.read())

        return user_list

    def persist_data(self, user_list: list):
        with open("user_list.json", "w") as f:
            json_string = jsonpickle.encode(user_list, indent=1)
            f.write(json_string)
