from cart.cartDAO import CartDAO
from cart.cartVO import CartVO
from book.bookDAO import BookDAO

class CartService:
    def __init__(self, cart_dao: CartDAO, book_dao: BookDAO):
        self.cart_dao = cart_dao
        self.book_dao = book_dao

    def add_to_cart(self, user_id, book_id, quantity):
        book_vo = self.book_dao.select_by_id(book_id)
        if not book_vo:
            print("❌ 존재하지 않는 도서입니다.")
            return
        cart = self.cart_dao.get_cart(user_id)
        if book_id in cart:
            cart[book_id].quantity += quantity
        else:
            cart[book_id] = CartVO(book_vo, quantity)
        print(f"🛒 [장바구니 담기] {book_vo.title} x {quantity}개")

    def show_cart(self, user_id):
        cart = self.cart_dao.get_cart(user_id)
        print(f"\n🛒 [{user_id}]님의 장바구니 리스트")
        if not cart:
            print("  장바구니가 비어 있습니다.")
            return
        total = 0
        for item in cart.values():
            sub = item.book_vo.price * item.quantity
            total += sub
            print(f"  - {item.book_vo.title} x {item.quantity}개 = {sub}원")
        print(f"  총 예상 결제금액: {total}원")

    def clear_cart(self, user_id):
        self.cart_dao.delete_all(user_id)
