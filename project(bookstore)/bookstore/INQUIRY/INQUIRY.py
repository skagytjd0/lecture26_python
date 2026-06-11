# Inquiry Service & DAO 통합 파일
from INQUIRY.INQUIRYVO import InquiryVO

class InquiryDAO:
    def __init__(self):
        self.inquiries = {}
        self.counter = 0

    def insert(self, user_id, title, content) -> InquiryVO:
        self.counter += 1
        inq_id = f"INQ-{self.counter:03d}"
        vo = InquiryVO(inq_id, user_id, title, content)
        self.inquiries[inq_id] = vo
        return vo

    def select_all(self):
        return list(self.categories_or_list() if hasattr(self, 'categories_or_list') else self.inquiries.values())

class InquiryService:
    def __init__(self, dao: InquiryDAO):
        self.dao = dao

    def leave_inquiry(self, user_id, title, content):
        vo = self.dao.insert(user_id, title, content)
        print(f"❓ [1:1문의] 등록 완료 -> 번호: {vo.inquiry_id} | 제목: {title}")

    def answer_inquiry(self, login_user, inquiry_id, reply_text):
        if not login_user or login_user.role != "관리자":
            print("🔒 [권한오류]")
            return
        inq = self.dao.inquiries.get(inquiry_id)
        if inq:
            inq.reply = reply_text
            print(f"📝 [문의답변] {inquiry_id}번에 대한 관리자 답변 등록 완료.")
