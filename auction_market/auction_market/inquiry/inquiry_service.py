from inquiry.inquiry_dao import InquiryDAO
from inquiry.inquiry import Inquiry

class InquiryService:
    def __init__(self, inquiry_dao):
        self.__dao = inquiry_dao
        self.inquiry_id_seq = 3000

    def register_inquiry(self, user_id, title, content):
        inquiry_id = str(self.inquiry_id_seq)
        self.inquiry_id_seq += 1
        new_inq = Inquiry(inquiry_id, user_id, title, content)
        return self.__dao.insert_inquiry(new_inq)

    def get_user_inquiries(self, user_id):
        all_inq = self.__dao.select_all_inquiries()
        result = []
        if all_inq:
            for i in range(len(all_inq)):
                if all_inq[i].get_user_id() == user_id:
                    result.append(all_inq[i])
        return result

    def get_all_inquiries(self):
        return self.__dao.select_all_inquiries()

    def update_inquiry(self, inquiry_id, user_id, title, content):
        inq = self.__dao.select_inquiry(inquiry_id)
        if inq and inq.get_user_id() == user_id and inq.get_status() == '답변대기':
            inq.set_title(title)
            inq.set_content(content)
            return True
        return False

    def answer_inquiry(self, inquiry_id, answer_text):
        inq = self.__dao.select_inquiry(inquiry_id)
        if inq:
            inq.set_answer(answer_text)
            inq.set_status('답변완료')
            return True
        return False
