class User:
    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def get_username(self) -> str:
        return self.username

    def get_email(self) -> str:
        return self.email

    def get_full_name(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_password(self, password):
        self.password = password

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return "(username: {}, email: {}, password: {}, full name: {})".format(self.username, self.email, self.password, self.get_full_name())

    def __eq__(self, o: object) -> bool:
        if o is None:
            return False

        if type(self) != type(o):
            return False

        return self.username == o.username or self.email == o.email
