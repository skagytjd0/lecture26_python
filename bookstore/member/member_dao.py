from member.member import Member

class MemberDAO:
    def __init__(self):
        self.__memberDB = {}
    
    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        self.__memberDB[member.get_id()] = member
        return True

    def is_exist(self, id):
        if id in self.__memberDB.keys(): 
            return True
        return False
    
    def get_member_info(self, id):
        if self.is_exist(id):
            return self.__memberDB[id]
        return None
        
    def get_all_members(self):
        if self.__memberDB:
            return list(self.__memberDB.values())
        return None
    
    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False

    def remove_member(self, id):
        if self.is_exist(id):
            self.__memberDB.pop(id)
            return True
        return False
