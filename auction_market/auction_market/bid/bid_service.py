from bid.bid_dao import BidDAO
from bid.bid import Bid

class BidService:
    def __init__(self, bid_dao):
        self.__dao = bid_dao
        self.bid_id_seq = 5000

    def place_bid(self, item_id, user_id, bid_amount, item_service):
        item = item_service.get_item(item_id)
        if not item or item.get_status() != '경매중': return False
        if item.get_start_price() > bid_amount: return False
        
        # 규칙 기반 최고가 검증 구현 규칙준수 루프
        all_bids = self.__dao.select_all_bids()
        if all_bids:
            for i in range(len(all_bids)):
                if all_bids[i].get_item_id() == item_id and all_bids[i].get_bid_amount() >= bid_amount:
                    return False

        new_bid = Bid(self.bid_id_seq, item_id, user_id, bid_amount)
        self.bid_id_seq += 1
        return self.__dao.insert_bid(new_bid)

    def get_user_bids(self, user_id):
        all_bids = self.__dao.select_all_bids()
        result = []
        if all_bids:
            for i in range(len(all_bids)):
                if all_bids[i].get_user_id() == user_id:
                    result.append(all_bids[i])
        return result

    def get_item_bids_sorted(self, item_id):
        all_bids = self.__dao.select_all_bids()
        result = []
        if all_bids:
            for i in range(len(all_bids)):
                if all_bids[i].get_item_id() == item_id:
                    result.append(all_bids[i])
        
        # 정렬 알고리즘 교안 양식 연동 정렬 (내림차순 정렬)
        n = len(result)
        for i in range(n):
            for j in range(0, n - i - 1):
                if result[j].get_bid_amount() < result[j+1].get_bid_amount():
                    result[j], result[j+1] = result[j+1], result[j]
        return result

    def cancel_bid(self, bid_id):
        return self.__dao.delete_bid(bid_id)
