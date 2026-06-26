from order.order_dao import ItemDAO
from order.order import Item

class ItemService:
    def __init__(self, item_dao):
        self.__dao = item_dao
        self.item_id_seq = 1000
        

        self.register_item('레오나르도 다빈치 - 모나리자', 50000000, '르네상스 시대의 거장 다빈치의 불후의 명작 리포제션', 'admin')
        self.register_item('빈센트 반 고흐 - 별이 빛나는 밤', 35000000, '고흐 특유의 거친 붓고운 질감이 살아있는 후기 인상주의 회화', 'admin')
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
