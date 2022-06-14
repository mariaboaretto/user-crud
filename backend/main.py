# from layout.user_management_window import *
# from PyQt5.QtWidgets import QApplication
from rest.server import Server
from rest.user_controller import UserController

if __name__ == '__main__':
    # user_service = UserServiceFactory.get()
    # app.run()

    server = Server()
    server.addController(UserController())
    # add more controllers

    server.run()

    # app = QApplication([])
    # main_window = UserManagementWindow(user_service)
    # main_window.start()
    # app.exec()
