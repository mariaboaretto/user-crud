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

    def filter_users(self, search_txt: str):
        matching_users = []

        for user in self.users:
            if search_txt in user.get_username() or search_txt in user.get_email():
                matching_users.append(user)

        return matching_users

    @staticmethod
    def __set_new_info(user: User, searched_term: str, first_name: str, last_name: str,
                       password: str):
        if user is None:
            raise Exception('User does not exist: {}'.format(searched_term))

        if first_name is None or first_name == '':
            raise Exception("Please insert user's first name")

        if last_name is None or last_name == '':
            raise Exception("Please insert user's last name")

        if password is None or password == '':
            raise Exception("Please insert a password")

        user.set_first_name(first_name)
        user.set_last_name(last_name)
        user.set_password(password)

    def update_user_by_username(self, username: str, first_name: str = None, last_name: str = None,
                                password: str = None):
        user = self.get_user_by_username(username)

        self.__set_new_info(user, username, first_name, last_name, password)

    def update_user_by_email(self, email: str, first_name: str = None, last_name: str = None, password: str = None):
        user = self.get_user_by_email(email)

        self.__set_new_info(user, email, first_name, last_name, password)
