class Inquiry:
    def __init__(self, inquiry_id, user_id, title, content):
        self.__inquiry_id = inquiry_id
        self.__user_id = user_id
        self.__title = title
        self.__content = content
        self.__answer = '없음'
        self.__status = '답변대기'

    def get_inquiry_id(self): return self.__inquiry_id
    def get_user_id(self): return self.__user_id
    def get_title(self): return self.__title
    def get_content(self): return self.__content
    def get_answer(self): return self.__answer
    def get_status(self): return self.__status

    def set_title(self, title): self.__title = title
    def set_content(self, content): self.__content = content
    def set_answer(self, answer): self.__answer = answer
    def set_status(self, status): self.__status = status

    def __str__(self):
        return f' 글번호: {self.__inquiry_id}\t작성자: {self.__user_id}\t제목: {self.__title}\t상태: {self.__status}\t답변: {self.__answer}'
