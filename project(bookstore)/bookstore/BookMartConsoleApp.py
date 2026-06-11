from member.memberDAO import MemberDAO
from member.memberService import MemberService
from book.bookDAO import BookDAO
from book.bookService import BookService
from cart.cartDAO import CartDAO
from cart.cartService import CartService
from order.orderDAO import OrderDAO
from order.orderService import OrderService
from INQUIRY.INQUIRY import InquiryDAO, InquiryService

def main():
    # DAOs
    member_dao = MemberDAO()
    book_dao = BookDAO()
    cart_dao = CartDAO()
    order_dao = OrderDAO()
    inquiry_dao = InquiryDAO()

    # Services
    member_service = MemberService(member_dao)
    book_service = BookService(book_dao)
    cart_service = CartService(cart_dao, book_dao)
    order_service = OrderService(order_dao, cart_dao)
    inquiry_service = InquiryService(inquiry_dao)

    print("==========================================================")
    print("      BookMart Console Application (VO Pattern)           ")
    print("==========================================================\n")

    # [USER-001] 회원 등록
    member_service.register("admin", "admin123", "김관리", "admin@mart.com", role="관리자")
    member_service.register("customer01", "pass123", "이유저", "user@mart.com", role="회원")

    # [USER-002] 로그인 처리 -> 결과물로 MemberVO 객체를 수신함
    admin_vo = member_service.login("admin", "admin123")
    user_vo = member_service.login("customer01", "pass123")

    # [BOOK-004] 관리자가 신규 도서(VO) 등록
    book_service.add_new_book(admin_vo, "BOOK-101", "파이썬 디자인 패턴", "전문서적", "IT", 32000, 20)
    book_service.add_new_book(admin_vo, "BOOK-102", "객체지향의 사실과 오해", "이론서적", "IT", 25000, 15)

    # [BOOK-003] 도서 검색
    book_service.search_books(keyword="오해")

    # [CART / ORDER] 유저 서비스 진행 시나리오
    if user_vo:
        uid = user_vo.user_id
        cart_service.add_to_cart(uid, "BOOK-101", 1)
        cart_service.add_to_cart(uid, "BOOK-102", 2)
        cart_service.show_cart(uid)

        # 주문 및 결제 연동
        order_vo = order_service.create_order(uid)
        if order_vo:
            cart_service.clear_cart(uid)

        # [INQUIRY] 1:1 고객 문의 접수 테스트
        inquiry_service.leave_inquiry(uid, "배송 문의", "책은 언제쯤 발송되나요?")
        
        # 관리자가 문의 답변 처리
        inquiry_service.answer_inquiry(admin_vo, "INQ-001", "내일 오전 일괄 출고 예정입니다.")

    # 관리자 최종 마스터 데이터 검증
    order_service.show_all_orders(admin_vo)

if __name__ == "__main__":
    main()
