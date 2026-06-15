from book.book import Book

class BookDAO:
    def __init__(self):
        self.__bookDB = {}
    
    def insert_book(self, book):
        book_no = book.get_book_no()
        if book_no not in self.__bookDB:
            self.__bookDB[book_no] = book
            return True
        return False

    def select_book_by_book_no(self, book_no):
        if book_no in self.__bookDB:
            return self.__bookDB[book_no]
        return None

    def select_all_books(self):
        book_list = list(self.__bookDB.values())
        if len(book_list):
            return book_list
        return None

    def update_book(self, book_no, book):
        if book_no in self.__bookDB:
            self.__bookDB[book_no] = book
            return True
        return False

    def delete_book(self, book_no):
        if book_no in self.__bookDB:
            self.__bookDB.pop(book_no)
            return True
        return False
