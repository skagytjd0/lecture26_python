class Winning:
    def __init__(self, win_id, item_id, user_id, final_amount):
        self.__win_id = win_id
        self.__item_id = item_id
        self.__user_id = user_id
        self.__final_amount = final_amount
        self.__status = '미입금'

    def get_win_id(self): return self.__win_id
    def get_item_id(self): return self.__item_id
    def get_user_id(self): return self.__user_id
    def get_final_amount(self): return self.__final_amount
    def get_status(self): return self.__status

    def set_status(self, status): self.__status = status

    def __str__(self):
        return f'낙찰번호: {self.__win_id}\t물품번호: {self.__item_id}\t낙찰자: {self.__user_id}\t최종가: {self.__final_amount}\t결제여부: {self.__status}'
