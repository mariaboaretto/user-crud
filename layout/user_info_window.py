from PyQt5.QtWidgets import QWidget, QFormLayout, QDialogButtonBox, QLineEdit


class UserInfoWindow:
    def __init__(self, window_title):
        self.window = QWidget()
        self.window.setGeometry(750, 300, 500, 200)
        self.window_title = window_title
        self.window.setWindowTitle(self.window_title)
        self.layout = QFormLayout()
        self.buttons = QDialogButtonBox()
        self.layout.addRow('First name:', QLineEdit())
        self.layout.addRow('Last name:', QLineEdit())
        self.layout.addRow('Email address:', QLineEdit())
        self.layout.addRow('Username:', QLineEdit())
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        self.layout.addRow('Password:', self.password_field)
        self.buttons.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.layout.addWidget(self.buttons)
        self.window.setLayout(self.layout)

    def show_window(self):
        self.window.show()
