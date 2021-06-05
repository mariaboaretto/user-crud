from PyQt5.QtWidgets import QMessageBox
from core.user_service import UserService
from core.user import User


class DeleteWarningMsg(QMessageBox):
    def __init__(self, user_service: UserService, user: User, window_title: str, window_txt, reload_table, parent=None):
        # Layout properties:
        super().__init__(parent)
        self.user_service = user_service
        self.window_title = window_title
        self.window_txt = window_txt
        self.user = user
        self.reload_table = reload_table

        # Setting layout:
        self.__init_widget()
        self.__init_window_layout()

    def __init_widget(self):
        self.setWindowTitle(self.window_title)
        self.setIcon(QMessageBox.Warning)

    def __init_window_layout(self):
        self.setText(self.window_txt)
        yes_btn = QMessageBox.Yes
        cancel_btn = QMessageBox.Cancel
        self.addButton(yes_btn)
        self.addButton(cancel_btn)
        self.accepted.connect(self.delete_user)
        self.rejected.connect(self.close)

    def delete_user(self):
        username = self.user.get_username()
        self.user_service.remove_user_by_username(username)
        self.reload_table()

    def start(self):
        self.show()
