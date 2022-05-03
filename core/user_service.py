from sqlite3 import SQLITE_DONE

from core.user import User
from core.user_repository import UserRepository


class UserService:
    def __init__(self):
        super().__init__()
        self.user_repo = UserRepository()

    def get_all_users(self) -> list[User]:
        return self.user_repo.select_all_users()

    def create_user(self, first_name: str, last_name: str, email: str, username: str, password: str):
        if first_name is None or first_name == '':
            raise Exception("Please insert user's first name")

        if last_name is None or last_name == '':
            raise Exception("Please insert user's last name")

        if email is None or email == '':
            raise Exception("Please insert user's email")

        if username is None or username == '':
            raise Exception("Please insert user's username")

        if password is None or password == '':
            raise Exception("Please insert user's password")

        self.user_repo.insert_user(first_name, last_name, email, username, password)

    def remove_user_by_id(self, user_id: int):
        self.user_repo.remove_user_by_user_id(user_id)

    def filter_users(self, search_txt: str):
        return self.user_repo.filter_users_by_search_text(search_txt)

    def update_user(self, user_id: int, first_name: str, last_name: str,
                    password: str):

        if first_name is None or first_name == '':
            raise Exception("Please insert user's first name")

        if last_name is None or last_name == '':
            raise Exception("Please insert user's last name")

        if password is None or password == '':
            raise Exception("Please insert a password")

        self.user_repo.update_user_by_user_id(user_id, first_name, last_name, password)

# CHA256
