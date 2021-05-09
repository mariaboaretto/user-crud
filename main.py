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
