class CartDAO:
    def __init__(self):
        self.carts = {}  # { user_id: { book_id: CartVO } }

    def get_cart(self, user_id):
        if user_id not in self.carts:
            self.carts[user_id] = {}
        return self.carts[user_id]

    def delete_all(self, user_id):
        self.carts[user_id] = {}
