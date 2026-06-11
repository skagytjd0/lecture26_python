from member.memberDAO import MemberDAO
from member.memberVO import MemberVO

class MemberService:
    def __init__(self, member_dao: MemberDAO):
        self.dao = member_dao

    def register(self, user_id, password, name, email, role="회원"):
        vo = MemberVO(user_id, password, name, email, role)
        if self.dao.insert(vo):
            print(f"🎉 [회원가입] 성공: {name}님 환영합니다.")
            return True
        print("❌ [회원가입] 실패: 중복된 ID입니다.")
        return False

    def login(self, user_id, password) -> MemberVO:
        vo = self.dao.select_by_id(user_id)
        if vo and vo.password == password:
            print(f"🔑 [로그인] 성공: {vo.name}님({vo.role})")
            return vo
        print("❌ [로그인] 실패: ID 또는 비밀번호 오류")
        return None
