import hashlib
from core.user import User
from core.user_repository import UserRepository


class UserService:
    def __init__(self):
        super().__init__()
        self.user_repo = UserRepository()

    @staticmethod
    def __hash_string(string: str) -> str:
        return hashlib.sha256(string.encode()).hexdigest()

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

        self.user_repo.insert_user(first_name, last_name, email, username, self.__hash_string(password))

    def remove_user_by_id(self, user_id: int):
        self.user_repo.remove_user_by_user_id(user_id)

    def filter_users(self, search_txt: str):
        return self.user_repo.filter_users_by_search_text(search_txt)

    def update_user_info(self, user_id: int, first_name: str = None, last_name: str = None):

        if first_name == "":
            raise Exception("Please insert user's first name")

        if last_name == "":
            raise Exception("Please insert user's last name.")

        self.user_repo.update_user_info(user_id, first_name, last_name)

    def update_user_password(self, user_id: int, current_password: str, new_password: str,
                             new_password_confirmation: str):
        if self.__hash_string(current_password) != self.user_repo.find_user_by_user_id(user_id).get_password():
            raise Exception("Current password is incorrect.")

        if new_password != new_password_confirmation:
            raise Exception("Passwords do not match.")

        self.user_repo.update_user_password(user_id, self.__hash_string(new_password))

    def find_user_by_user_id(self, user_id: int):
        return self.user_repo.find_user_by_user_id(user_id)
