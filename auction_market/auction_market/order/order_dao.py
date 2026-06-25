from order.order import Item

class ItemDAO:
    def __init__(self):
        self.__itemDB = {}

    def insert_item(self, item):
        self.__itemDB[item.get_item_id()] = item
        return True

    def select_item_by_id(self, item_id):
        if item_id in self.__itemDB: return self.__itemDB[item_id]
        return None

    def select_all_items(self):
        if self.__itemDB: return list(self.__itemDB.values())
        return None

    def update_item(self, item_id, item):
        if item_id in self.__itemDB:
            self.__itemDB[item_id] = item
            return True
        return False

    def delete_item(self, item_id):
        if item_id in self.__itemDB:
            self.__itemDB.pop(item_id)
            return True
        return False
