class Cart:
    def __init__(self, member_id, book_no, title, qty, price):
        self.__member_id = member_id
        self.__book_no = book_no
        self.__title = title
        self.__qty = qty
        self.__price = price

    def get_member_id(self):
        return self.__member_id
    def get_book_no(self):
        return self.__book_no
    def get_title(self):
        return self.__title
    def get_qty(self):
        return self.__qty
    def get_price(self):
        return self.__price
    
    def set_qty(self, qty):
        self.__qty = qty

    def __str__(self):
        return f'도서번호 = {self.__book_no}, 도서명 = {self.__title}, 수량 = {self.__qty}, 단가 = {self.__price}, 총액 = {self.__qty * self.__price}'
