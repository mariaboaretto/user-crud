from PyQt5.QtWidgets import QTableWidget, QHeaderView, QPushButton, QHBoxLayout, QWidget, QTableWidgetItem
from core.user_service import UserService
from layout.user_info_dialog import UserInfoDialog


class UserListTable(QTableWidget):
    def __init__(self, user_service: UserService):
        # Layout properties:
        super().__init__()
        self.user_service = user_service

        # Setting layout
        self.__set_table()
        self.reload_user_list()

    def __set_table(self):
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Full name', 'Email address', 'Username', 'Actions'])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def reload_user_list(self):
        user_list = self.user_service.get_all_users()
        row = 0
        self.setRowCount(len(user_list))
        self.verticalHeader().setDefaultSectionSize(45)

        for user in user_list:
            # Action buttons:
            delete_btn = QPushButton('Delete')
            delete_btn.setStyleSheet('background-color: #b30000; color: white; font-weight: bold')
            edit_btn = QPushButton('Edit')
            edit_btn.setStyleSheet('background-color: #0077b3; color: white; font-weight: bold')
            # edit_user_window = UserInfoDialog('Edit user', self.user_service)
            # edit_btn.clicked.connect(lambda: edit_user_window.start())
            button_layout = QHBoxLayout()
            button_layout.addWidget(edit_btn)
            button_layout.addWidget(delete_btn)
            buttons_widget = QWidget()
            buttons_widget.setLayout(button_layout)
            self.setCellWidget(row, 3, buttons_widget)
            # Loading users in table:
            self.setItem(row, 0, QTableWidgetItem(user.get_full_name()))
            self.setItem(row, 1, QTableWidgetItem(user.get_email()))
            self.setItem(row, 2, QTableWidgetItem(user.get_username()))
            row = row + 1
