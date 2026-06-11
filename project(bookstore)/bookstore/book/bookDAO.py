from book.bookVO import BookVO

class BookDAO:
    def __init__(self):
        self.books = {}  # Memory DB

    def insert(self, vo: BookVO):
        self.books[vo.book_id] = vo

    def select_by_id(self, book_id) -> BookVO:
        return self.books.get(book_id)

    def select_all(self):
        return list(self.books.values())

    def update(self, book_id, **kwargs):
        vo = self.books.get(book_id)
        if vo:
            for key, value in kwargs.items():
                if hasattr(vo, key):
                    setattr(vo, key, value)
            return True
        return False
