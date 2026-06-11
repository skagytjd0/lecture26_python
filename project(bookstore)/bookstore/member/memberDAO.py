from member.memberVO import MemberVO

class MemberDAO:
    def __init__(self):
        self.users = {}  # Memory DB (key: user_id, value: MemberVO)

    def insert(self, vo: MemberVO):
        if vo.user_id in self.users:
            return False
        self.users[vo.user_id] = vo
        return True

    def select_by_id(self, user_id) -> MemberVO:
        return self.users.get(user_id)

    def select_all(self):
        return list(self.users.values())
