from bid.bid import Bid

class BidDAO:
    def __init__(self):
        self.__bidDB = {}

    def insert_bid(self, bid):
        self.__bidDB[bid.get_bid_id()] = bid
        return True

    def select_all_bids(self):
        if self.__bidDB: return list(self.__bidDB.values())
        return None

    def delete_bid(self, bid_id):
        if bid_id in self.__bidDB:
            self.__bidDB.pop(bid_id)
            return True
        return False
