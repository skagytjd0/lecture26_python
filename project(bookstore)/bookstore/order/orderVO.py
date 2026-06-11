from datetime import datetime

class OrderVO:
    def __init__(self, order_id, user_id, order_items, total_amount):
        self.order_id = order_id
        self.user_id = user_id
        self.order_items = order_items  # List of OrderItemVO
        self.total_amount = total_amount
        self.status = "주문완료"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
