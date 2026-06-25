from order.order_dao import ItemDAO
from order.order import Item

class ItemService:
    def __init__(self, item_dao):
        self.__dao = item_dao
        self.item_id_seq = 1000

    def register_item(self, title, start_price, description, seller):
        item_id = str(self.item_id_seq)
        self.item_id_seq += 1
        item = Item(item_id, title, description, start_price, seller)
        self.__dao.insert_item(item)
        return True

    def get_all_items(self):
        return self.__dao.select_all_items()

    def get_item(self, item_id):
        return self.__dao.select_item_by_id(item_id)

    def cancel_auction(self, item_id):
        item = self.__dao.select_item_by_id(item_id)
        if item:
            item.set_status('경매취소')
            return True
        return False
