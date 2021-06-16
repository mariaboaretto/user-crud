from layout.user_management_window import *
from core.user_service import UserService
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    user_service = UserService()
    app = QApplication([])
    main_window = UserManagementWindow(user_service)
    main_window.start()
    app.exec()
