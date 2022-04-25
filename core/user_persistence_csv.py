from core.user_persistence_interface import UserPersistenceInterface
from core.user import User


class UserPersistenceCSV(UserPersistenceInterface):
    def load_data(self) -> list[User]:
        user_list = []

        with open("user_list.csv", "r") as f:
            for line in f:
                line = line.strip("\n")
                x = line.split(";")
                new_user = User(x[0], x[1], x[2], x[3], x[4])
                user_list.append(new_user)

        return user_list

    def persist_data(self, user_list: list):
        with open("user_list.csv", "w") as f:
            for user in user_list:
                f.write(f"{user.get_first_name()};{user.get_last_name()};{user.get_email()};{user.get_username()};"
                        f"{user.get_password()}\n")
