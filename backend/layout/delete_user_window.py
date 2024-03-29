from PyQt5.QtWidgets import QMessageBox
from core.user_service import UserService


class DeleteWarningMsg(QMessageBox):
    def __init__(self, user_service: UserService, user, window_title: str, window_txt,
                 success_function=None, parent=None):
        # Layout properties:
        super().__init__(parent)
        self.user_service = user_service
        self.window_title = window_title
        self.window_txt = window_txt
        self.user = user
        self.success_function = success_function

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
        self.user_service.remove_user_by_id(self.user.user_id)

        if self.success_function is not None:
            self.success_function()

    def start(self):
        self.show()
