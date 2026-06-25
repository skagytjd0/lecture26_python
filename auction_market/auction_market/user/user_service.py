from user.user_dao import UserDAO
from user.user import User

class UserService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self, user_dao):
        self.__dao = user_dao
        self.user_seq = 1
        # 관리자 기본 계정 등록 (USER-002)
        self.join(User(0, UserService.ADMIN_ID, UserService.ADMIN_PASSWORD, '최고관리자', '010-0000-0000', 'admin@market.com', '본부'))
        self.current_user = None

    def join(self, user):
        if self.__dao.is_exist(user.get_id()): return False
        if user.get_id() != UserService.ADMIN_ID:
            user._User__user_no = self.user_seq
            self.user_seq += 1
        return self.__dao.insert_user(user)

    def login(self, id, password):
        user = self.__dao.get_user_info(id)
        if user and user.get_password() == password:
            self.current_user = id
            return True
        return False

    def logout(self):
        self.current_user = None

    def view_user_info(self, id):
        return self.__dao.get_user_info(id)

    def update_user_info(self, id, password, name, mobile, email, address):
        user = self.__dao.get_user_info(id)
        if user:
            user.set_password(password)
            user.set_name(name)
            user.set_mobile(mobile)
            user.set_email(email)
            user.set_address(address)
            return True
        return False

    def remove_user(self, id):
        return self.__dao.remove_user(id)

    def list_users(self):
        return self.__dao.get_all_users()
