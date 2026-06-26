class Item:
    def __init__(self, item_id, title, description, start_price, seller):
        self.__item_id = item_id
        self.__title = title
        self.__description = description
        self.__start_price = start_price
        self.__status = '경매중'
        self.__seller = seller

    def get_item_id(self): return self.__item_id
    def get_title(self): return self.__title
    def get_description(self): return self.__description
    def get_start_price(self): return self.__start_price
    def get_status(self): return self.__status
    def get_seller(self): return self.__seller

    def set_status(self, status): self.__status = status

    def __str__(self):
        return f'품번: {self.__item_id}\t물품명: {self.__title}\t시작값: {self.__start_price}\t상태: {self.__status}\t등록자: {self.__seller}'
