class User:
    def __init__(self, user_no, id, password, name, mobile, email, address):
        self.__user_no = user_no
        self.__id = id
        self.__password = password
        self.__name = name
        self.__mobile = mobile
        self.__email = email
        self.__address = address

    def get_user_no(self): return self.__user_no
    def get_id(self): return self.__id
    def get_password(self): return self.__password
    def get_name(self): return self.__name
    def get_mobile(self): return self.__mobile
    def get_email(self): return self.__email
    def get_address(self): return self.__address

    def set_password(self, password): self.__password = password
    def set_name(self, name): self.__name = name
    def set_mobile(self, mobile): self.__mobile = mobile
    def set_email(self, email): self.__email = email
    def set_address(self, address): self.__address = address

    def __str__(self):
        return f'[{self.__user_no}] ID: {self.__id}\t이름: {self.__name}\t연락처: {self.__mobile}\t이메일: {self.__email}\t주소: {self.__address}'
