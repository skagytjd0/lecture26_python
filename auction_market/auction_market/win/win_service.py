from win.win_dao import WinningDAO
from win.win import Winning

class WinningService:
    def __init__(self, winning_dao):
        self.__dao = winning_dao
        self.win_id_seq = 9000

    def close_auction_and_select_winner(self, item_id, bid_service, item_service):
        item = item_service.get_item(item_id)
        if not item or item.get_status() != '경매중': return False

        sorted_bids = bid_service.get_item_bids_sorted(item_id)
        if not sorted_bids or len(sorted_bids) == 0:
            item.set_status('유찰종료')
            return False

        highest_bid = sorted_bids[0]
        win_id = str(self.win_id_seq)
        self.win_id_seq += 1

        new_win = Winning(win_id, item_id, highest_bid.get_user_id(), highest_bid.get_bid_amount())
        self.__dao.insert_winning(new_win)
        item.set_status('낙찰완료')
        return True

    def get_user_winnings(self, user_id):
        all_wins = self.__dao.select_all_winnings()
        result = []
        if all_wins:
            for i in range(len(all_wins)):
                if all_wins[i].get_user_id() == user_id:
                    result.append(all_wins[i])
        return result

    def get_all_winnings(self):
        return self.__dao.select_all_winnings()

    def cancel_winning(self, win_id, item_service):
        win = self.__dao.select_winning(win_id)
        if win:
            item = item_service.get_item(win.get_item_id())
            if item: item.set_status('경매중')
            win.set_status('낙찰취소')
            return True
        return False
