from PyQt5.QtWidgets import QTableWidget, QHeaderView, QPushButton, QHBoxLayout, QWidget, QTableWidgetItem
from core.user_service import UserService
from layout.user_info_dialog import UserInfoDialog
from layout.delete_user_window import DeleteWarningMsg


class UserListTable(QTableWidget):
    def __init__(self, user_service: UserService, user_list, success_function):
        # Layout properties:
        super().__init__()
        self.user_service = user_service
        self.user_list = user_list
        self.success_function = success_function

        # Setting layout
        self.__set_table()
        self.reload_user_list()

    def __set_table(self):
        self.setColumnCount(4)
        self.setHorizontalHeaderLabels(['Full name', 'Email address', 'Username', 'Actions'])
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def set_user_list(self, user_list):
        self.user_list = user_list

    def reload_user_list(self):
        row = 0
        self.setRowCount(len(self.user_list))
        self.verticalHeader().setDefaultSectionSize(45)

        for user in self.user_list:
            edit_user_window = UserInfoDialog('Edit user', self.user_service, self, self.success_function, user=user)
            delete_user_window = DeleteWarningMsg(self.user_service, user, 'WARNING!',
                                                  'Are you sure you want to delete this user?'
                                                  'This action cannot be undone.', self.success_function, self)

            # Action buttons:
            delete_btn = QPushButton('Delete')
            delete_btn.setStyleSheet('background-color: #b30000; color: white; font-weight: bold')
            delete_btn.clicked.connect(delete_user_window.start)
            edit_btn = QPushButton('Edit')
            edit_btn.clicked.connect(edit_user_window.start)
            edit_btn.setStyleSheet('background-color: #0077b3; color: white; font-weight: bold')

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
