from order.orderVO import OrderVO

class OrderDAO:
    def __init__(self):
        self.orders = {}
        self.counter = 0

    def insert(self, user_id, order_items, total_amount) -> OrderVO:
        self.counter += 1
        order_id = f"ORD-{self.counter:03d}"
        vo = OrderVO(order_id, user_id, order_items, total_amount)
        self.orders[order_id] = vo
        return vo

    def select_all(self):
        return list(self.orders.values())
