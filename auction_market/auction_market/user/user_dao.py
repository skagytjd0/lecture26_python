from user.user import User

class UserDAO:
    def __init__(self):
        self.__memberDB = {}

    def insert_user(self, user):
        if self.is_exist(user.get_id()): return False
        self.__memberDB[user.get_id()] = user
        return True

    def is_exist(self, id):
        if id in self.__memberDB.keys(): return True
        return False

    def get_user_info(self, id):
        if self.is_exist(id): return self.__memberDB[id]
        return None

    def get_all_users(self):
        if self.__memberDB: return list(self.__memberDB.values())
        return None

    def remove_user(self, id):
        if self.is_exist(id):
            self.__memberDB.pop(id)
            return True
        return False
