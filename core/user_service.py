from core.user import User


class UserService:
    def __init__(self):
        self.users = []

    def get_all_users(self) -> list[User]:
        return self.users

    def create_user(self, first_name: str, last_name: str, email: str, username: str, password: str):
        for user in self.users:
            if user.get_username() == username:
                raise Exception('Username already exists: {}'.format(username))

            if user.get_email() == email:
                raise Exception('Email already exists: {}'.format(email))

        new_user = User(first_name, last_name, email, username, password)
        self.users.append(new_user)

    def remove_user_by_username(self, username: str):
        for user in self.users:
            if user.get_username() == username:
                self.users.remove(user)

    def remove_user_by_email(self, email: str):
        for user in self.users:
            if user.get_email() == email:
                self.users.remove(user)

    def get_user_by_username(self, username: str):
        for user in self.users:
            if user.get_username() == username:
                return user

    def get_user_by_email(self, email: str):
        for user in self.users:
            if user.get_email() == email:
                return user

    def set_new_info(self, user: User, searched_term: str, first_name: str = None, last_name: str = None,
                     password: str = None):
        if user is None:
            raise Exception('User does not exist: {}'.format(searched_term))

        if first_name is not None:
            user.set_first_name(first_name)

        if last_name is not None:
            user.set_last_name(last_name)

        if password is not None:
            user.set_password(password)

    def update_user_by_username(self, username: str, first_name: str = None, last_name: str = None,
                                password: str = None):
        user = self.get_user_by_username(username)

        self.set_new_info(user, username, first_name, last_name, password)

    def update_user_by_email(self, email: str, first_name: str = None, last_name: str = None, password: str = None):
        user = self.get_user_by_email(email)

        self.set_new_info(user, email, first_name, last_name, password)
