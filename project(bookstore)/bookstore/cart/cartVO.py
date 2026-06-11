from book.bookVO import BookVO

class CartVO:
    def __init__(self, book_vo: BookVO, quantity: int):
        self.book_vo = book_vo
        self.quantity = quantity
