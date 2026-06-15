from inquiry.inquiry_dao import InquiryDAO
from inquiry.inquiry import Inquiry

class InquiryService:
    inquiry_no_seq = 1

    def __init__(self, inquiry_dao):
        self.__dao = inquiry_dao

    def register_inquiry(self, inquiry):
        inquiry.set_inquiry_no(InquiryService.inquiry_no_seq)
        InquiryService.inquiry_no_seq += 1
        return self.__dao.insert_inquiry(inquiry)

    def get_all_inquiries(self):
        return self.__dao.select_all_inquiries()

    def get_user_inquiries(self, author_id):
        return self.__dao.select_inquiries_by_author(author_id)

    def answer_inquiry(self, inquiry_no, reply_content):
        inquiry = self.__dao.select_inquiry_by_no(inquiry_no)
        if inquiry:
            inquiry.set_reply(reply_content)
            return self.__dao.update_inquiry(inquiry_no, inquiry)
        return False
