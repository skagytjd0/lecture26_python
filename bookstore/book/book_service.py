from book.book_dao import BookDAO
from book.book import Book

class BookService:
    book_no_seq = 1001

    def __init__(self, book_dao):
        self.__dao = book_dao
        self.__init_default_books()
    def __init_default_books(self):
            from book.book import Book
            self.create_book(Book(0, '파이썬 알고리즘 기초', '이혜정', 25000, 10))
            self.create_book(Book(0, '자료구조 대요', '이혜정', 28000, 5))
            self.create_book(Book(0, '인공지능 소프트웨어공학', '김폴리', 30000, 0))
            
    def create_book(self, book):
        book.set_book_no(str(BookService.book_no_seq)) 
        BookService.book_no_seq += 1 
        return self.__dao.insert_book(book)

    def get_all_books(self):
        return self.__dao.select_all_books()

    def get_book_info(self, book_no):
        return self.__dao.select_book_by_book_no(book_no)
        
    def update_book_stock(self, book_no, qty, order_type):
        book = self.__dao.select_book_by_book_no(book_no)
        if book:
            if order_type == 'BUY':
                if book.get_stock() >= qty:
                    book.set_stock(book.get_stock() - qty)
                    return self.__dao.update_book(book_no, book)
            elif order_type == 'CANCEL':
                book.set_stock(book.get_stock() + qty)
                return self.__dao.update_book(book_no, book)
        return False
