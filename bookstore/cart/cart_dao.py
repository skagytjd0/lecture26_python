from cart.cart import Cart

class CartDAO:
    def __init__(self):
        self.__cartDB = {} # 회원ID : [Cart 객체들]

    def insert_cart_item(self, cart_item):
        mid = cart_item.get_member_id()
        if mid not in self.__cartDB:
            self.__cartDB[mid] = []
        
        item_list = self.__cartDB[mid]
        for i in range(len(item_list)):
            if item_list[i].get_book_no() == cart_item.get_book_no():
                item_list[i].set_qty(item_list[i].get_qty() + cart_item.get_qty())
                return True
                
        self.__cartDB[mid].append(cart_item)
        return True

    def select_cart_by_member(self, member_id):
        if member_id in self.__cartDB:
            return self.__cartDB[member_id]
        return None

    def delete_cart_item(self, member_id, book_no):
        if member_id in self.__cartDB:
            item_list = self.__cartDB[member_id]
            for i in range(len(item_list)):
                if item_list[i].get_book_no() == book_no:
                    item_list.pop(i)
                    return True
        return False

    def clear_member_cart(self, member_id):
        if member_id in self.__cartDB:
            self.__cartDB[member_id] = []
            return True
        return False
