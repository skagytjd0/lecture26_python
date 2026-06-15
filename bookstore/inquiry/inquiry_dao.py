from inquiry.inquiry import Inquiry

class InquiryDAO:
    def __init__(self):
        self.__inquiryDB = {}

    def insert_inquiry(self, inquiry):
        inquiry_no = inquiry.get_inquiry_no()
        if inquiry_no not in self.__inquiryDB:
            self.__inquiryDB[inquiry_no] = inquiry
            return True
        return False

    def select_inquiry_by_no(self, inquiry_no):
        if inquiry_no in self.__inquiryDB:
            return self.__inquiryDB[inquiry_no]
        return None

    def select_all_inquiries(self):
        inquiry_list = list(self.__inquiryDB.values())
        if len(inquiry_list):
            return inquiry_list
        return None

    def select_inquiries_by_author(self, author_id):
        inquiry_list = []
        for inquiry in self.__inquiryDB.values():
            if inquiry.get_author_id() == author_id:
                inquiry_list.append(inquiry)
        if len(inquiry_list):
            return inquiry_list
        return None

    def update_inquiry(self, inquiry_no, inquiry):
        if inquiry_no in self.__inquiryDB:
            self.__inquiryDB[inquiry_no] = inquiry
            return True
        return False
