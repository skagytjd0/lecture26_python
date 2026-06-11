class MemberVO:
    def __init__(self, user_id, password, name, email, role="회원"):
        self.user_id = user_id
        self.password = password
        self.name = name
        self.email = email
        self.role = role  # 회원, 관리자
