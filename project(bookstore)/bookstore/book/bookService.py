from book.bookDAO import BookDAO
from book.bookVO import BookVO

class BookService:
    def __init__(self, book_dao: BookDAO):
        self.dao = book_dao

    def add_new_book(self, login_user, book_id, title, series, category, price, stock):
        if not login_user or login_user.role != "관리자":
            print("🔒 [권한오류] 관리자 전용 기능입니다.")
            return
        vo = BookVO(book_id, title, series, category, price, stock)
        self.dao.insert(vo)
        print(f"📚 [도서추가] {title} 등록 완료.")

    def search_books(self, keyword="", category=""):
        print(f"\n🔎 [도서검색] 키워드: '{keyword}' | 분류: '{category}'")
        results = []
        for b in self.dao.select_all():
            if (keyword in b.title or keyword in b.series) and (not category or b.category == category):
                results.append(b)
                print(f"  -> [{b.book_id}] {b.title} | {b.price}원 (재고:{b.stock})")
        return results
