# from layout.user_info_window import UserInfoWindow
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMenu, QMenuBar, QAction, QLabel, \
    QLineEdit, QPushButton
from layout.user_list_table import UserListTable


# # Delete user alert:
# delete_user_alert = QMessageBox(QMessageBox.Warning, 'WARNING!', 'Are you sure you want to delete this user? '
#                                                                  'This action cannot be undone.')
# delete_user_alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
#
# create_user_window = UserInfoWindow('Create new user')
# edit_user_window = UserInfoWindow('Edit user info')
#
#
# # Update user info window:
# def edit_window():
#     edit_user_window.show_window()
#
#
# # Create user info window:
# def new_user_window():
#     create_user_window.show_window()
#
#
# def delete_user_window():
#     delete_user_alert.show()


# Main screen:
class UserManagementWindow(QWidget):
    def __init__(self, user_service):
        super().__init__()
        # setting window properties:
        self.box = QVBoxLayout()
        self.user_service = user_service

        # setting up window
        self.__init_widget()
        self.__init_box()

    def __init_widget(self):
        self.setGeometry(100, 100, 1366, 768)
        self.setWindowTitle('User Management System')
        self.setStyleSheet('QHBoxLayout { background-color: #F00; }')
        menu_bar = QMenuBar(self)
        # Help menu:
        help_menu = QMenu('&Help', menu_bar)
        menu_bar.addMenu(help_menu)
        about_section = QAction('&About', help_menu)
        help_menu.addAction(about_section)

    def __init_box(self):
        # Outer layout box:
        title_lbl = QLabel('User Management System')
        title_lbl.setStyleSheet('color: #000000; font-size: 20px; margin-top: 30px; margin-bottom: 20px;'
                                'margin-left: 10px')
        self.box.addWidget(title_lbl)

        # Toolbar:
        h_box = QHBoxLayout()
        h_box.setContentsMargins(10, 0, 10, 0)
        # Create user button:
        create_user_btn = QPushButton('Create new user')
        create_user_btn.setStyleSheet('background-color: #269900; color: white; font-weight: bold')
        # create_user_btn.clicked.connect(new_user_window)

        #     Search user field:
        search_field = QLineEdit()
        search_field.setPlaceholderText('Type to search user...')
        # Adding to toolbar layout:
        h_box.addWidget(search_field)
        h_box.addWidget(create_user_btn)
        # Table layout:
        user_info_layout = QVBoxLayout()
        user_info_layout.setContentsMargins(10, 0, 10, 10)
        user_lst_lbl = QLabel('User list:')
        user_info_layout.addWidget(user_lst_lbl)
        table = UserListTable(self.user_service)
        user_info_layout.addWidget(table)

        # Adding to outer layout:
        self.box.addLayout(h_box)
        self.box.addLayout(user_info_layout)
        self.setLayout(self.box)

    def start(self):
        self.showMaximized()
