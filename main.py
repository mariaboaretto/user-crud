from layout.user_management_window import *
from core.user_service import UserService

if __name__ == '__main__':
    user_service = UserService()
    user_service.create_user('Maria', 'Boaretto', 'mariaboarettocampos@gmail.com', 'mauazera', 'aaaa')
    user_service.create_user('Caik', 'Henrique', 'carloshenrique.dev@gmail.com', 'caiik_h', 'aaaa')
    user_service.create_user('Aya', 'Bissinho', 'aya.bissinho@gmail.com', 'ayaaa', 'aaaa')
    app = QApplication([])
    main_window = UserManagementWindow(user_service)
    main_window.start()
    app.exec()
    pass

# # User info layout:
#         user_info_layout = QVBoxLayout()
#         user_info_layout.setContentsMargins(10, 0, 10, 10)
#         user_lst_lbl = QLabel('User list:')
#         user_info_table = QTableWidget()
#         user_info_table.setColumnCount(4)
#         user_info_table.setHorizontalHeaderLabels(['Full name', 'Email address', 'Username', 'Actions'])
#         user_info_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         user_list = self.user_service.get_all_users()
#         user_info_table.setRowCount(len(user_list))
#         user_info_table.verticalHeader().setDefaultSectionSize(45)
#         # Buttons:
#         delete_btn = QPushButton('Delete')
#         delete_btn.setStyleSheet('background-color: #b30000; color: white; font-weight: bold')
#         edit_btn = QPushButton('Edit')
#         edit_btn.setStyleSheet('background-color: #0077b3; color: white; font-weight: bold')
#         button_layout = QHBoxLayout()
#         button_layout.addWidget(edit_btn)
#         button_layout.addWidget(delete_btn)
#         # delete_btn.clicked.connect(delete_user_window)
#         # edit_btn.clicked.connect(edit_window)
#         buttons_widget = QWidget()
#         buttons_widget.setLayout(button_layout)
#         user_info_table.setCellWidget(0, 3, buttons_widget)
