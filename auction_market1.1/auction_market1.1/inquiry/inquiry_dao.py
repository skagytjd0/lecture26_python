from inquiry.inquiry import Inquiry

class InquiryDAO:
    def __init__(self):
        self.__inquiryDB = {}

    def insert_inquiry(self, inquiry):
        self.__inquiryDB[inquiry.get_inquiry_id()] = inquiry
        return True

    def select_all_inquiries(self):
        if self.__inquiryDB: return list(self.__inquiryDB.values())
        return None

    def select_inquiry(self, inquiry_id):
        if inquiry_id in self.__inquiryDB: return self.__inquiryDB[inquiry_id]
        return None

    def update_inquiry(self, inquiry_id, inquiry):
        if inquiry_id in self.__inquiryDB:
            self.__inquiryDB[inquiry_id] = inquiry
            return True
        return False
