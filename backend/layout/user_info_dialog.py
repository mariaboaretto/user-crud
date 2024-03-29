from PyQt5.QtWidgets import QFormLayout, QDialogButtonBox, QLineEdit, QDialog, QMessageBox, QLabel, QPushButton
from core.user_service import UserService
from layout.edit_password_window import EditPasswordWindow


class UserInfoDialog(QDialog):
    def __init__(self, window_title: str, user_service: UserService, parent=None, success_function=None, user=None):
        super().__init__(parent)
        self.window_title = window_title
        self.form_layout = QFormLayout()
        self.user_service = user_service
        self.success_function = success_function
        self.user = user

        self.__init_widget()
        self.__init_form_layout()

    def __init_widget(self):
        self.setGeometry(750, 300, 500, 200)
        self.setWindowTitle(self.window_title)

    def __init_form_layout(self):
        # Buttons
        buttons = QDialogButtonBox()
        save_button = QDialogButtonBox.Save
        cancel_button = QDialogButtonBox.Cancel
        buttons.setStandardButtons(save_button | cancel_button)

        # User data layout:
        first_name_field = QLineEdit()
        last_name_field = QLineEdit()
        email_field = QLineEdit()
        username_field = QLineEdit()
        password_field = QLineEdit()
        password_field.setEchoMode(QLineEdit.Password)

        # Filling fields in edit user window:
        if self.user is not None:
            # Edit Password btn for edit user window
            edit_password_btn = QPushButton("Edit Password")
            # Creating Edit Password window
            edit_password_btn.clicked.connect(self.__create_edit_password_window)

            uneditable_field_style = 'background-color: #d9d9d9; color: #4d4d4d'
            first_name_field.setText(self.user.get_first_name())
            last_name_field.setText(self.user.get_last_name())
            email_field.setText(self.user.get_email())
            email_field.setReadOnly(True)
            email_field.setStyleSheet(uneditable_field_style)
            username_field.setText(self.user.get_username())
            username_field.setStyleSheet(uneditable_field_style)
            username_field.setReadOnly(True)

        self.form_layout.addRow('First name:', first_name_field)
        self.form_layout.addRow('Last name:', last_name_field)
        self.form_layout.addRow('Email address:', email_field)
        self.form_layout.addRow('Username', username_field)

        # Placing password field if creating user, edit password btn if editing user
        if self.user is None:
            self.form_layout.addRow('Password:', password_field)
        else:
            self.form_layout.addRow(edit_password_btn, None)

        self.form_layout.addWidget(buttons)
        self.setLayout(self.form_layout)

        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(lambda: self.create_or_edit_user(first_name_field, last_name_field, email_field,
                                                                  username_field, password_field))

    def create_or_edit_user(self, first_name_field, last_name_field, email_field, username_field, password_field):
        first_name = first_name_field.text()
        last_name = last_name_field.text()
        email = email_field.text()
        username = username_field.text()
        password = password_field.text()

        try:

            msg = ""

            if self.user is None:
                self.user_service.create_user(first_name, last_name, email, username, password)
                msg = 'User created successfully!'

            else:
                self.user_service.update_user_info(self.user.user_id, first_name, last_name)
                msg = 'User updated successfully!'

            return_value = QMessageBox.information(self, 'Successful!', msg, QMessageBox.Ok)

            if return_value == QMessageBox.Ok:
                self.close()

            if self.success_function is not None:
                self.success_function()

        except Exception as e:
            error_msg = QMessageBox(parent=self)
            error_msg.setWindowTitle('ERROR!')
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setText('Error - {}'.format(e))
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()

    def __create_edit_password_window(self):
        edit_password_window = EditPasswordWindow(self, "Edit Password", self.user_service, self.user)
        edit_password_window.start()

    def start(self):
        self.show()
