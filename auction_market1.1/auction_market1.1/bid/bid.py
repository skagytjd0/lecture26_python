class Bid:
    def __init__(self, bid_id, item_id, user_id, bid_amount):
        self.__bid_id = bid_id
        self.__item_id = item_id
        self.__user_id = user_id
        self.__bid_amount = bid_amount

    def get_bid_id(self): return self.__bid_id
    def get_item_id(self): return self.__item_id
    def get_user_id(self): return self.__user_id
    def get_bid_amount(self): return self.__bid_amount

    def __str__(self):
        return f'입찰번호: {self.__bid_id}\t물품번호: {self.__item_id}\t입찰자: {self.__user_id}\t입찰가: {self.__bid_amount}'
