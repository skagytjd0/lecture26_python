
import sys
from user.user import User
from user.user_dao import UserDAO
from user.user_service import UserService
from order.order import Item
from order.order_dao import ItemDAO
from order.order_service import ItemService
from bid.bid import Bid
from bid.bid_dao import BidDAO
from bid.bid_service import BidService
from win.win import Winning
from win.win_dao import WinningDAO
from win.win_service import WinningService
from inquiry.inquiry import Inquiry
from inquiry.inquiry_dao import InquiryDAO
from inquiry.inquiry_service import InquiryService

class ConsoleMarket:
    start_menu = ['종료', '로그인', '회원가입']
    user_menu = ['로그아웃', '경매물품목록', '경매물품등록', '경매입찰하기', '내입찰내역조회', '내낙찰내역조회', '문의사항등록', '내문의목록조회', '내정보조회', '내정보수정', '회원탈퇴']
    admin_menu = ['로그아웃', '회원목록', '회원정보수정(관리)', '악성회원추방', '경매품등록(관리자)', '경매취소처리', '상품별입찰현황', '부정입찰취소', '낙찰자선정(마감)', '전체낙찰내역관리', '낙찰취소처리', '전체문의목록', '문의답변등록', '문의답변수정']

    def __init__(self):
        self.usv = UserService(UserDAO())
        self.isv = ItemService(ItemDAO())
        self.bsv = BidService(BidDAO())
        self.wsv = WinningService(WinningDAO())
        self.qsv = InquiryService(InquiryDAO())

    def main(self):
        while True:
            if self.usv.current_user == None:
                menu = self.select_menu(ConsoleMarket.start_menu)
                if menu == 0: break
                elif menu == 1: self.menu_login()
                elif menu == 2: self.menu_join()
            elif self.usv.current_user == UserService.ADMIN_ID:
                menu = self.select_menu(ConsoleMarket.admin_menu)
                if menu == 0: self.usv.logout()
                elif menu == 1: self.menu_list_users()
                elif menu == 2: self.menu_admin_update_user()
                elif menu == 3: self.menu_kick_user()
                elif menu == 4: self.menu_register_item()
                elif menu == 5: self.menu_cancel_order()
                elif menu == 6: self.menu_item_bids()
                elif menu == 7: self.menu_cancel_bid()
                elif menu == 8: self.menu_close_auction()
                elif menu == 9: self.menu_all_winnings()
                elif menu == 10: self.menu_cancel_winning()
                elif menu == 11: self.menu_all_inquiries()
                elif menu == 12: self.menu_answer_inquiry()
                elif menu == 13: self.menu_answer_inquiry()
            else:
                menu = self.select_menu(ConsoleMarket.user_menu)
                if menu == 0: self.usv.logout()
                elif menu == 1: self.menu_list_items()
                elif menu == 2: self.menu_register_item()
                elif menu == 3: self.menu_place_bid()
                elif menu == 4: self.menu_my_bids()
                elif menu == 5: self.menu_my_winnings()
                elif menu == 6: self.menu_add_inquiry()
                elif menu == 7: self.menu_my_inquiries()
                elif menu == 8: self.menu_my_info()
                elif menu == 9: self.menu_update_my_info()
                elif menu == 10: self.menu_withdraw()

    def select_menu(self, menu_list):
        print('\n=================== MENU ===================')
        for i in range(len(menu_list)):
            print(f'{i}. {menu_list[i]}', end='   ')
        print('\n============================================')
        try:
            return int(input('>> 메뉴 선택: '))
        except ValueError:
            return -1

    def menu_join(self):
        id = input('ID: ')
        pw = input('PW: ')
        name = input('이름: ')
        mobile = input('모바일: ')
        email = input('이메일: ')
        addr = input('주소: ')
        if self.usv.join(User(0, id, pw, name, mobile, email, addr)):
            print('>> 회원가입 완료.')
        else:
            print('>> 이미 존재하는 ID입니다.')

    def menu_login(self):
        id = input('ID: ')
        pw = input('PW: ')
        if self.usv.login(id, pw):
            print(f'>> {id}님 로그인 성공.')
        else:
            print('>> 인증에 실패했습니다.')

    def menu_my_info(self):
        u = self.usv.view_user_info(self.usv.current_user)
        if u: print(u)

    def menu_update_my_info(self):
        pw = input('새 PW: ')
        name = input('새 이름: ')
        mobile = input('새 모바일: ')
        email = input('새 이메일: ')
        addr = input('새 주소: ')
        self.usv.update_user_info(self.usv.current_user, pw, name, mobile, email, addr)
        print('>> 수정 완료.')

    def menu_withdraw(self):
        if self.usv.remove_user(self.usv.current_user):
            self.usv.logout()
            print('>> 탈퇴 완료 처리되었습니다.')

    def menu_list_users(self):
        ul = self.usv.list_users()
        if ul:
            for i in range(len(ul)): print(ul[i])

    def menu_admin_update_user(self):
        mid = input('수정할 회원 ID: ')
        pw = input('새 PW: ')
        name = input('새 이름: ')
        mobile = input('새 모바일: ')
        email = input('새 이메일: ')
        addr = input('새 주소: ')
        if self.usv.update_user_info(mid, pw, name, mobile, email, addr):
            print('>> 관리자 권한 회원 정보 수정 완료.')

    def menu_kick_user(self):
        mid = input('추방할 악성 회원 ID: ')
        if self.usv.remove_user(mid):
            print('>> 해당 회원을 탈퇴 및 강제 추방하였습니다.')

    def menu_register_item(self):
        title = input('상품명: ')
        try:
            price = int(input('시작 가격: '))
            desc = input('상세 설명: ')
            self.isv.register_item(title, price, desc, self.usv.current_user)
            print('>> 경매 물품 업로드 완료.')
        except ValueError:
            print('>> 숫자로 입력해야 합니다.')

    def menu_list_items(self):
        il = self.isv.get_all_items()
        if il:
            for i in range(len(il)): print(il[i])
        else:
            print('>> 등록된 경매 상품이 존재하지 않습니다.')

    def menu_cancel_order(self):
        item_id = input('중단 및 취소할 경매품 번호: ')
        if self.isv.cancel_auction(item_id):
            print('>> 해당 경매 처리가 취소/무효화되었습니다.')

    def menu_place_bid(self):
        item_id = input('입찰할 경매품 번호: ')
        try:
            amount = int(input('입찰 제시 금액: '))
            if self.bsv.place_bid(item_id, self.usv.current_user, amount, self.isv):
                print('>> 입찰이 정상 응찰되었습니다.')
            else:
                print('>> 입찰 불가 (시작값 미달, 최고가 미달 혹은 진행중이 아님).')
        except ValueError:
            print('>> 올바른 정수 가격을 입력하세요.')

    def menu_my_bids(self):
        bl = self.bsv.get_user_bids(self.usv.current_user)
        for i in range(len(bl)): print(bl[i])

    def menu_item_bids(self):
        item_id = input('조회할 상품 번호: ')
        bl = self.bsv.get_item_bids_sorted(item_id)
        for i in range(len(bl)): print(bl[i])

    def menu_cancel_bid(self):
        try:
            bid_id = int(input('강제 삭제 취소할 입찰 고유 번호: '))
            if self.bsv.cancel_bid(bid_id):
                print('>> 해당 입찰건이 데이터베이스에서 무효화 삭제되었습니다.')
        except ValueError:
            print('>> 정수를 입력해야 합니다.')

    def menu_close_auction(self):
        item_id = input('마감 처리할 경매품 번호: ')
        if self.wsv.close_auction_and_select_winner(item_id, self.bsv, self.isv):
            print('>> 최종 최고가 입찰자 낙찰 판정 완료 및 객체 적재 완료.')
        else:
            print('>> 마감 처리 실패 또는 유찰 종료되었습니다.')

    def menu_my_winnings(self):
        wl = self.wsv.get_user_winnings(self.usv.current_user)
        for i in range(len(wl)): print(wl[i])

    def menu_all_winnings(self):
        wl = self.wsv.get_all_winnings()
        if wl:
            for i in range(len(wl)): print(wl[i])

    def menu_cancel_winning(self):
        win_id = input('취소 처리할 낙찰/주문 고유번호: ')
        if self.wsv.cancel_winning(win_id, self.isv):
            print('>> 낙찰 무효 처리 및 경매 상태 롤백 완료.')

    def menu_add_inquiry(self):
        title = input('문의 제목: ')
        content = input('문의 내용: ')
        self.qsv.register_inquiry(self.usv.current_user, title, content)
        print('>> 1:1 고객 문의가 접수 등록되었습니다.')

    def menu_my_inquiries(self):
        ql = self.qsv.get_user_bids(self.usv.current_user) if hasattr(self.qsv, 'get_user_bids') else self.qsv.get_user_quiries(self.usv.current_user) if hasattr(self.qsv, 'get_user_quiries') else self.qsv.get_user_inquiries(self.usv.current_user)
        for i in range(len(ql)): print(ql[i])

    def menu_all_inquiries(self):
        ql = self.qsv.get_all_inquiries()
        if ql:
            for i in range(len(ql)): print(ql[i])

    def menu_answer_inquiry(self):
        inq_id = input('답변 처리할 문의 글 번호: ')
        ans = input('작성할 관리자 답변 내용: ')
        if self.qsv.answer_inquiry(inq_id, ans):
            print('>> 문의에 대한 답변 등록/수정이 완료되었습니다.')

if __name__ == '__main__':
    market = ConsoleMarket()
    market.main()
