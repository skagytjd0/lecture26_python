from member.member import Member
from member.member_dao import MemberDAO
from member.member_service import MemberService
from book.book import Book
from book.book_dao import BookDAO
from book.book_service import BookService
from cart.cart import Cart
from cart.cart_dao import CartDAO
from cart.cart_service import CartService
from inquiry.inquiry import Inquiry
from inquiry.inquiry_dao import InquiryDAO
from inquiry.inquiry_service import InquiryService

class ConsoleBookstore:
    start_menu = ['종료', '로그인', '회원가입']
    user_menu = ['로그아웃', '도서목록조회', '장바구니보기', '도서주문하기', '고객문의', '내정보']
    cart_menu = ['돌아가기', '장바구니내역조회', '장바구니품목추가', '품목삭제', '장바구니전체구매결제']
    user_inquiry_menu = ['돌아가기', '문의등록', '내문의목록']
    member_myinfo_menu = ['돌아가기', '비밀번호수정', '회원탈퇴']
    admin_menu = ['로그아웃', '회원관리', '도서관리', '문의관리']
    admin_book_menu = ['돌아가기', '전체도서목록', '도서등록']
    admin_member_menu = ['돌아가기', '회원목록', '회원정보조회', '회원강퇴']
    admin_inquiry_menu = ['돌아가기', '전체문의목록', '문의답변등록']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.bsv = BookService(BookDAO())
        self.csv = CartService(CartDAO())
        self.isv = InquiryService(InquiryDAO())


    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    def show_welcome(self):
        print('======== Console Bookstore (Cart Integrated System) ==========')

    def say_goodbye(self):
        print('>> Console Bookstore를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print()
        for i in range(len(menu_list)):
            print(f'{i}.{menu_list[i]}', end='  ')
        print()
        try:
            choice = int(input('선택 > '))
            if 0 <= choice < len(menu_list):
                return choice
            return -1
        except ValueError:
            return -1

    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.start_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()

    def menu_join(self):
        print('\n[ 회원 가입 ]')
        mid = input('ID : ')
        password = input('PASSWORD : ')
        name = input('NAME : ')
        member = Member(mid, password, name)
        if self.msv.join(member):
            print('회원가입 성공')
        else:
            print('이미 존재하는 ID입니다.')

    def menu_login(self):
        print('\n[ 로그인 ]')
        mid = input('ID : ')
        password = input('PASSWORD : ')
        if self.msv.login(mid, password):
            print(f'{mid}님 로그인 되었습니다.')
            if mid == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_user_menu()
        else:
            print('ID 혹은 PASSWORD가 틀립니다.')

    def run_user_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.user_menu)
            if menu == 0:
                self.msv.logout()
                break
            elif menu == 1:
                self.menu_list_books()
            elif menu == 2:
                self.run_cart_menu()
            elif menu == 3:
                self.menu_order_book()
            elif menu == 4:
                self.run_user_inquiry_menu()
            elif menu == 5:
                self.run_my_info_menu()

    def menu_list_books(self):
        print('\n[ 도서 목록 ]')
        b_list = self.bsv.get_all_books()
        for i in range(len(b_list)):
                    print(b_list[i])

    def run_cart_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.cart_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_view_cart()
            elif menu == 2:
                self.menu_add_cart()
            elif menu == 3:
                self.menu_remove_cart_item()
            elif menu == 4:
                self.menu_checkout_cart()

    def menu_view_cart(self):
        print('\n[ 장바구니 내역 조회 ]')
        c_list = self.csv.get_cart_list(self.msv.current_user)
        if c_list == None or len(c_list) == 0:
            print('장바구니가 비어 있습니다.')
        else:
            for i in range(len(c_list)):
                print(c_list[i])

    def menu_add_cart(self):
        print('\n[ 장바구니 품목 추가 ]')
        b_no = input('담을 도서번호 : ')
        book = self.bsv.get_book_info(b_no)
        if not book:
            print('존재하지 않는 도서번호입니다.')
            return
        qty = int(input('수량 입력 : '))
        if qty <= 0:
            print('1개 이상의 수량을 입력하십시오.')
            return
        if book.get_stock() < qty:
            print('재고가 부족하여 장바구니에 담을 수 없습니다.')
            return
        
        cart_item = Cart(self.msv.current_user, b_no, book.get_title(), qty, book.get_price())
        self.csv.add_to_cart(cart_item)
        print('상품이 장바구니에 추가되었습니다.')

    def menu_remove_cart_item(self):
        print('\n[ 장바구니 품목 삭제 ]')
        b_no = input('삭제할 도서번호 : ')
        if self.csv.remove_item(self.msv.current_user, b_no):
            print('장바구니에서 정상 삭제되었습니다.')
        else:
            print('장바구니에 일치하는 도서가 없습니다.')

    def menu_checkout_cart(self):
        print('\n[ 장바구니 전체 보관 상품 결제 ]')
        c_list = self.csv.get_cart_list(self.msv.current_user)
        if c_list == None or len(c_list) == 0:
            print('장바구니에 결제할 품목이 없습니다.')
            return
        
        for i in range(len(c_list)):
            book = self.bsv.get_book_info(c_list[i].get_book_no())
            if book.get_stock() < c_list[i].get_qty():
                print(f'상품 [{book.get_title()}]의 재고 부족으로 결제가 불가능합니다.')
                return

        for i in range(len(c_list)):
            item = c_list[i]
            self.bsv.update_book_stock(item.get_book_no(), item.get_qty(), 'BUY')
            print(f'[결제영수증] 도서명: {item.get_title()}, 수량: {item.get_qty()}, 금액: {item.get_qty() * item.get_price()}')
            
        self.csv.clear_cart(self.msv.current_user)
        print('>> 장바구니 결제가 성공하여 장바구니를 비웠습니다.')

    def menu_order_book(self):
        print('\n[ 도서 즉시 주문하기]')
        b_no = input('구매할 도서번호 : ')
        book = self.bsv.get_book_info(b_no)
        if not book:
            print('존재하지 않는 도서번호입니다.')
            return
        qty = int(input('주문 수량 입력 : '))
        if qty <= 0:
            print('올바른 수량을 입력하십시오.')
            return
        if book.get_stock() < qty:
            print('재고 부족으로 인해 주문을 실행할 수 없습니다.')
            return
            
        # 임시 장바구니 연산 (함수 탈출 시 완전 자동 삭제 및 영속 셋 누수 방지)
        temporary_cart_list = []
        temp_item = Cart(self.msv.current_user, b_no, book.get_title(), qty, book.get_price())
        temporary_cart_list.append(temp_item)
        
        print('-> 주문 도서가 일회성 임시 장바구니 세션에 할당되었습니다. 즉시 승인합니다.')
        for i in range(len(temporary_cart_list)):
            target_item = temporary_cart_list[i]
            self.bsv.update_book_stock(target_item.get_book_no(), target_item.get_qty(), 'BUY')
            print(f'[즉시주문 영수증] 제목: {target_item.get_title()}, 수량: {target_item.get_qty()}, 결제액: {target_item.get_qty() * target_item.get_price()}')
        
        print('>> [성공] 즉시 구매 승인이 완료되었으며, 임시 장바구니 세션이 파기되었습니다.')

    def run_user_inquiry_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.user_inquiry_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_register_inquiry()
            elif menu == 2:
                self.menu_list_my_inquiries()

    def menu_register_inquiry(self):
        print('\n[ 고객 문의 등록 ]')
        title = input('문의 제목 : ')
        content = input('문의 내용 : ')
        inquiry = Inquiry(self.msv.current_user, title, content)
        if self.isv.register_inquiry(inquiry):
            print('문의사항이 정상적으로 등록되었습니다.')

    def menu_list_my_inquiries(self):
        print('\n[ 내 문의 목록 조회 ]')
        iq_list = self.isv.get_user_inquiries(self.msv.current_user)
        if iq_list == None or len(iq_list) == 0:
            print('등록된 문의 내역이 없습니다.')
        else:
            for i in range(len(iq_list)):
                print(iq_list[i])

    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.member_myinfo_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_update_password()
            elif menu == 2:
                if self.menu_delete_membership():
                    return

    def menu_update_password(self):
        print('\n[ 비밀번호 변경 ]')
        org_pw = input('기존 비밀번호 : ')
        new_pw = input('새 비밀번호 : ')
        if self.msv.update_member_password(self.msv.current_user, org_pw, new_pw):
            print('비밀번호 변경 완료')
        else:
            print('변경 실패')

    def menu_delete_membership(self):
        print('\n[ 회원 탈퇴 ]')
        chk = input('정말 탈퇴하시겠습니까? (y/n) : ')
        if chk == 'y' or chk == 'Y':
            self.msv.remove_member(self.msv.current_user)
            print('탈퇴 완료')
            return True
        return False

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.admin_menu)
            if menu == 0:
                self.msv.logout()
                break
            elif menu == 1:
                self.run_admin_member_menu()
            elif menu == 2:
                self.run_admin_book_menu()
            elif menu == 3:
                self.run_admin_inquiry_menu()

    def run_admin_book_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.admin_book_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_books()
            elif menu == 2:
                self.menu_register_book()

    def menu_register_book(self):
        print('\n[ 도서 등록 ]')
        title = input('도서 제목 : ')
        author = input('도서 저자 : ')
        price = int(input('도서 가격 : '))
        stock = int(input('초기 재고량 : '))
        book = Book(0, title, author, price, stock)
        if self.bsv.create_book(book):
            print('도서 등록 성공')

    def run_admin_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.admin_member_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_members()
            elif menu == 2:
                self.menu_view_member_info()
            elif menu == 3:
                self.menu_delete_member()

    def menu_list_members(self):
        print('\n[ 회원 목록 ]')
        m_list = self.msv.list_members()
        if m_list:
            for i in range(len(m_list)):
                print(m_list[i])

    def menu_view_member_info(self):
        mid = input('조회 ID : ')
        member = self.msv.view_member_info(mid)
        if member: print(member)

    def menu_delete_member(self):
        mid = input('강퇴 ID : ')
        if mid != MemberService.ADMIN_ID:
            self.msv.remove_member(mid)
            print('강퇴 완료')

    def run_admin_inquiry_menu(self):
        while True:
            menu = self.select_menu(ConsoleBookstore.admin_inquiry_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_all_inquiries()
            elif menu == 2:
                self.menu_answer_inquiry()

    def menu_list_all_inquiries(self):
        print('\n[ 관리자 - 전체 문의 목록 ]')
        iq_list = self.isv.get_all_inquiries()
        if iq_list:
            for i in range(len(iq_list)):
                print(iq_list[i])

    def menu_answer_inquiry(self):
        iq_no = int(input('문의번호 : '))
        reply = input('답변 내용 : ')
        self.isv.answer_inquiry(iq_no, reply)
        print('답변 등록 완료')

if __name__ == '__main__':
    bookstore = ConsoleBookstore()
    bookstore.main()
