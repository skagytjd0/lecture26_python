from order.orderDAO import OrderDAO
from order.orderitemVO import OrderItemVO
from cart.cartDAO import CartDAO

class OrderService:
    def __init__(self, order_dao: OrderDAO, cart_dao: CartDAO):
        self.order_dao = order_dao
        self.cart_dao = cart_dao

    def create_order(self, user_id):
        cart = self.cart_dao.get_cart(user_id)
        if not cart:
            print("❌ 장바구니가 비어 주문이 불가합니다.")
            return None
        
        order_items = []
        total_amount = 0
        for item in cart.values():
            order_items.append(OrderItemVO(item.book_vo, item.quantity))
            total_amount += item.book_vo.price * item.quantity

        order_vo = self.order_dao.insert(user_id, order_items, total_amount)
        print(f"📦 [주문체결] 완료! 주문번호: {order_vo.order_id} (총 {total_amount}원)")
        return order_vo

    def show_all_orders(self, login_user):
        if not login_user or login_user.role != "관리자":
            print("🔒 [권한오류]")
            return
        print("\n--- [관리자] 시스템 전체 주문 데이터 현황 ---")
        for o in self.order_dao.select_all():
            print(f"- [{o.order_id}] 유저: {o.user_id} | 금액: {o.total_amount}원 | 상태: {o.status}")
