from book.bookVO import BookVO

class OrderItemVO:
    def __init__(self, book_vo: BookVO, quantity: int):
        self.book_vo = book_vo
        self.quantity = quantity
        self.order_price = book_vo.price
