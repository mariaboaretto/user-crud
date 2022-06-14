from PyQt5.QtWidgets import QFormLayout, QDialogButtonBox, QLineEdit, QDialog, QMessageBox
from core.user_service import UserService
from core.user import User


class EditPasswordWindow(QDialog):
    def __init__(self, parent, window_title, user_service: UserService, user: User):
        super().__init__(parent)
        self.window_title = window_title
        self.form_layout = QFormLayout()
        self.user_service = user_service
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

        # Fields
        current_password_field = QLineEdit()
        current_password_field.setEchoMode(QLineEdit.Password)
        new_password_field = QLineEdit()
        new_password_field.setEchoMode(QLineEdit.Password)
        new_password_confirmation_field = QLineEdit()
        new_password_confirmation_field.setEchoMode(QLineEdit.Password)

        # Setting rows
        self.form_layout.addRow("Current Password:", current_password_field)
        self.form_layout.addRow("New Password:", new_password_field)
        self.form_layout.addRow("Confirm New Password", new_password_confirmation_field)

        self.form_layout.addWidget(buttons)
        self.setLayout(self.form_layout)

        # Button events
        buttons.rejected.connect(self.reject)
        buttons.accepted.connect(lambda: self.update_password(current_password_field,
                                                              new_password_field, new_password_confirmation_field))

    def update_password(self, current_password_field, new_password_field, password_confirmation_field):
        try:
            self.user_service.update_user_password(self.user.user_id, current_password_field.text(),
                                                   new_password_field.text(), password_confirmation_field.text())
            return_value = QMessageBox.information(self, 'Successful!', "Password Updated Successfully!",
                                                   QMessageBox.Ok)
            if return_value == QMessageBox.Ok:
                self.close()

        except Exception as e:
            error_msg = QMessageBox(parent=self)
            error_msg.setWindowTitle('ERROR!')
            error_msg.setIcon(QMessageBox.Critical)
            error_msg.setText('Error - {}'.format(e))
            error_msg.setStandardButtons(QMessageBox.Ok)
            error_msg.show()

    def start(self):
        self.show()
