# from layout.user_info_window import UserInfoWindow
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QMenu, QMenuBar, QAction, QLabel, \
    QLineEdit, QPushButton
from layout.user_list_table import UserListTable
from core.user_service import UserService
from layout.user_info_dialog import UserInfoDialog


# Main screen:
class UserManagementWindow(QWidget):
    def __init__(self, user_service: UserService):
        super().__init__()
        # setting window properties:
        self.box = QVBoxLayout()
        self.user_service = user_service
        self.search_field = QLineEdit()
        self.table = UserListTable(self.user_service, self.user_service.get_all_users(),
                                   lambda: self.reload_table_and_clear_filter(self.search_field))

        # setting up window
        self.__init_widget()
        self.__init_box()

    def __init_widget(self):
        self.setGeometry(100, 100, 1366, 768)
        self.setWindowTitle('User Management System')
        menu_bar = QMenuBar(self)
        # Help menu:
        help_menu = QMenu('&Help', menu_bar)
        menu_bar.addMenu(help_menu)
        about_section = QAction('&About', help_menu)
        # about_section.triggered.connect()
        help_menu.addAction(about_section)

    def reload_table_and_clear_filter(self, search_field: QLineEdit):
        self.table.set_user_list(self.user_service.get_all_users())
        self.table.reload_user_list()
        search_field.clear()

    def create_user_window(self, search_field):
        create_user_widget = UserInfoDialog('Create new user', self.user_service, self,
                                            lambda: self.reload_table_and_clear_filter(self.search_field))
        create_user_widget.start()

    def search_user(self, search_text):
        matching_users = self.user_service.filter_users(search_text)
        self.table.set_user_list(matching_users)
        self.table.reload_user_list()

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
        create_user_btn.clicked.connect(lambda: self.create_user_window(self.search_field))

        # Search user field:
        self.search_field.setPlaceholderText('Type to search user...')
        # Search user button:
        search_btn = QPushButton('Search')
        search_btn.setStyleSheet('background-color: #808080; color: white; font-weight: bold')
        search_btn.clicked.connect(lambda: self.search_user(self.search_field.text()))

        # Adding to toolbar layout:
        h_box.addWidget(self.search_field)
        h_box.addWidget(search_btn)
        h_box.addWidget(create_user_btn)

        # Table layout:
        user_info_layout = QVBoxLayout()
        user_info_layout.setContentsMargins(10, 0, 10, 10)
        user_lst_lbl = QLabel('User list:')
        user_info_layout.addWidget(user_lst_lbl)
        user_info_layout.addWidget(self.table)

        # Adding to outer layout:
        self.box.addLayout(h_box)
        self.box.addLayout(user_info_layout)
        self.setLayout(self.box)

    def start(self):
        self.showMaximized()
