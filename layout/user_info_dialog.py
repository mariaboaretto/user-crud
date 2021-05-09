from PyQt5.QtWidgets import QFormLayout, QDialogButtonBox, QLineEdit, QDialog, QMessageBox
from core.user_service import UserService


class UserInfoDialog(QDialog):
    def __init__(self, window_title: str, user_service: UserService, parent=None):
        super().__init__(parent)
        self.window_title = window_title
        self.form_layout = QFormLayout()
        self.user_service = user_service

        self.__init_widget()
        self.__init_form_layout()

    def __init_widget(self):
        self.setGeometry(750, 300, 500, 200)
        self.setWindowTitle(self.window_title)

    def __init_form_layout(self):
        # Buttons
        buttons = QDialogButtonBox()
        ok_button = QDialogButtonBox.Save
        cancel_button = QDialogButtonBox.Cancel
        buttons.setStandardButtons(ok_button | cancel_button)

        # User data layout:
        first_name_field = QLineEdit()
        last_name_field = QLineEdit()
        email_field = QLineEdit()
        username_field = QLineEdit()
        password_field = QLineEdit()
        password_field.setEchoMode(QLineEdit.Password)

        self.form_layout.addRow('First name:', first_name_field)
        self.form_layout.addRow('Last name:', last_name_field)
        self.form_layout.addRow('Email address:', email_field)
        self.form_layout.addRow('Username', username_field)
        self.form_layout.addRow('Password:', password_field)
        self.form_layout.addWidget(buttons)
        self.setLayout(self.form_layout)

        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(lambda: self.create_user(first_name_field, last_name_field, email_field,
                                                          username_field, password_field))

    def create_user(self, first_name_field, last_name_field, email_field, username_field, password_field):
        first_name = first_name_field.text()
        last_name = last_name_field.text()
        email = email_field.text()
        username = username_field.text()
        password = password_field.text()

        try:
            self.user_service.create_user(first_name, last_name, email, username, password)
        except Exception as e:
            print('{}'.format(e))

    def start(self):
        self.show()
