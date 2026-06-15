class Inquiry:
    def __init__(self, author_id, title, content):
        self.__inquiry_no = 0
        self.__author_id = author_id
        self.__title = title
        self.__content = content
        self.__reply = '답변 대기 중'

    def get_inquiry_no(self):
        return self.__inquiry_no
    def get_author_id(self):
        return self.__author_id
    def get_title(self):
        return self.__title
    def get_content(self):
        return self.__content
    def get_reply(self):
        return self.__reply

    def set_inquiry_no(self, inquiry_no):
        self.__inquiry_no = inquiry_no
    def set_reply(self, reply):
        self.__reply = reply

    def __str__(self):
        return f'문의번호 = {self.__inquiry_no}, 작성자 = {self.__author_id}, 제목 = {self.__title}, 내용 = {self.__content}\n   └▶ 답변: {self.__reply}'
