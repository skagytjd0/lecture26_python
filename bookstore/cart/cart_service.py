from cart.cart_dao import CartDAO
from cart.cart import Cart

class CartService:
    def __init__(self, cart_dao):
        self.__dao = cart_dao

    def add_to_cart(self, cart_item):
        return self.__dao.insert_cart_item(cart_item)

    def get_cart_list(self, member_id):
        return self.__dao.select_cart_by_member(member_id)

    def remove_item(self, member_id, book_no):
        return self.__dao.delete_cart_item(member_id, book_no)

    def clear_cart(self, member_id):
        return self.__dao.clear_member_cart(member_id)
