from core.user_service import UserService


class UserServiceFactory:
    __instance = None

    # Returns an instance of User Service
    @staticmethod
    def get():
        if UserServiceFactory.__instance is None:
            UserServiceFactory()

        return UserServiceFactory.__instance.user_service

    def __init__(self):
        self.user_service = UserService()

        if UserServiceFactory.__instance is None:
            UserServiceFactory.__instance = self

