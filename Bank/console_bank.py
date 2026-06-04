from member.member import Member
from member.member_dao import MemberDAO
from member.member_service import MemberService
from account.account import Account
from account.account_dao import AccountDAO
from account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['로그아웃', '계좌목록', '입금', '출금', '계좌생성', '계좌해지', '내정보']
    member_myinfo_menu = ['돌아가기', '비밀번호수정', '회원탈퇴']
    admin_menu = ['로그아웃', '회원관리', '계좌관리']
    admin_account_menu = ['돌아가기', '전체계좌목록', '회원별계좌목록']
    admin_member_menu = ['돌아가기', '회원목록', '회원정보조회', '회원강퇴']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def main(self):
        self.show_welcome()
        self.run_start_menu()
        self.say_goodbye()

    def show_welcome(self):
        print('========skagytjd Console Bank ==========')

    def say_goodbye(self):
        print('>> skagytjd Console Bank를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print()
        print('-' * 40)
        for i in range(len(menu_list)):
            print(f'{i}.{menu_list[i]}', end='  ')
        print()
        print('-' * 40)
        try:
            num = int(input('>> 메뉴 선택 : '))
            if 0 <= num < len(menu_list):
                return num
            else:
                print('없는 메뉴입니다.')
                return -1
        except Exception:
            print('숫자를 입력해주세요.')
            return -1

    def run_start_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.start_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()

    def menu_join(self):
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        name = input('> 회원명 입력 : ')
        member = Member(id, password, name)
        if self.msv.join(member):
            print('회원가입이 완료되었습니다.')
        else:
            print('회원가입에 실패하였습니다.')

    def menu_login(self):
        id = input('> 아이디 입력 : ')
        password = input('> 비밀번호 입력 : ')
        if self.msv.login(id, password):
            print(f'{self.msv.view_member_info(id).get_name()}님 환영합니다 !')
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()   
            else:
                self.run_banking_menu() 
        else:
            print('로그인에 실패하였습니다.')

    def menu_logout(self):
        return self.msv.logout()

    def run_banking_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.banking_menu)
            if menu == 0:
                self.menu_logout()
                print('로그아웃 되었습니다.')
                return
            elif menu == 1:
                self.menu_list_my_accounts()
            elif menu == 2:
                self.menu_deposite()
            elif menu == 3:
                self.menu_withdraw()
            elif menu == 4:
                self.menu_create_account()
            elif menu == 5:
                self.menu_delete_account()
            elif menu == 6:
                self.menu_myinfo()

    def menu_list_my_accounts(self):
        print('\n[ 내 계좌 목록 ]')
        ac_list = self.asv.get_members_accounts(self.msv.current_user)
        if ac_list == None or len(ac_list) == 0:
            print('개설된 계좌가 없습니다.')
        else:
            for i in range(len(ac_list)):
                print(ac_list[i])

    def menu_deposite(self):
        print('\n[ 입금 ]')
        account_no = input('입금할 계좌번호 : ')
        try:
            amount = int(input('입금할 금액 : '))
            if self.asv.deposit(account_no, amount):
                print('입금이 완료되었습니다.')
            else:
                print('없는 계좌이거나 입금에 실패했습니다.')
        except Exception:
            print('금액은 숫자로 입력해주세요.')

    def menu_withdraw(self):
        print('\n[ 출금 ]')
        account_no = input('출금할 계좌번호 : ')
        password = input('계좌 비밀번호 : ')
        try:
            amount = int(input('출금할 금액 : '))
            self.asv.withdraw(self.msv.current_user, account_no, amount, password)
            print('출금이 완료되었습니다.')
        except LookupError:
            print('존재하지 않는 계좌입니다.')
        except KeyError:
            print('소유자 정보나 비밀번호가 일치하지 않습니다.')
        except ValueError:
            print('잔액이 부족합니다.')
        except Exception:
            print('출금에 실패했습니다.')

    def menu_create_account(self):
        print('\n[ 계좌 생성 ]')
        password = input('새 계좌 비밀번호 설정 : ')
        try:
            balance = int(input('초기 입금 금액 : '))
            account = Account(0, self.msv.current_user, balance, password)
            if self.asv.create_account(account):
                print('계좌가 정상적으로 생성되었습니다.')
            else:
                print('계좌 생성에 실패했습니다.')
        except Exception:
            print('금액은 숫자로 입력해주세요.')

    def menu_delete_account(self):
        print('\n[ 계좌 해지 ]')
        account_no = input('해지할 계좌번호 : ')
        password = input('계좌 비밀번호 : ')
        try:
            if self.asv.delete_account(self.msv.current_user, account_no, password):
                print('계좌 해지가 완료되었습니다.')
            else:
                print('계좌 해지에 실패했습니다.')
        except LookupError:
            print('존재하지 않는 계좌입니다.')
        except KeyError:
            print('소유자 정보나 비밀번호가 일치하지 않습니다.')
        except ValueError:
            print('잔액이 남아있어 해지할 수 없습니다.')
        except Exception:
            print('계좌 해지에 실패했습니다.')

    def menu_myinfo(self):
        self.run_my_info_menu()

    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.member_myinfo_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_update_password()
            elif menu == 2:
                self.menu_delete_membership()
                return

    def menu_view_myinfo(self):
        member = self.msv.view_member_info(self.msv.current_user)
        if member:
            print(member)

    def menu_update_password(self):
        print('\n[ 비밀번호 수정 ]')
        org_password = input('기존 비밀번호 : ')
        new_password = input('새로운 비밀번호 : ')
        if self.msv.update_member_password(self.msv.current_user, org_password, new_password):
            print('비밀번호를 수정하였습니다.')
        else:
            print('비밀번호 수정에 실패하였습니다.')

    def menu_delete_membership(self):
        print('\n[ 회원 탈퇴 ]')
        confirm = input('정말 탈퇴하시겠습니까? (y/n) : ')
        if confirm == 'y' or confirm == 'Y':
            if self.msv.remove_member(self.msv.current_user):
                print('회원 탈퇴가 완료되었습니다.')
                self.menu_logout()
            else:
                print('회원 탈퇴에 실패하였습니다.')

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_menu)
            if menu == 0:
                self.menu_logout()
                print('로그아웃 되었습니다.')
                return
            elif menu == 1:
                self.menu_manage_members()
            elif menu == 2:
                self.menu_manage_accounts()

    def menu_manage_members(self):
        self.run_admin_member_menu()

    def menu_manage_accounts(self):
        self.run_admin_account_menu()

    def run_admin_account_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_account_menu)
            if menu == 0:
                return
            elif menu == 1:
                self.menu_list_all_accounts()
            elif menu == 2:
                self.menu_list_member_accounts()

    def menu_list_all_accounts(self):
        print('\n[ 전체 계좌 목록 ]')
        all_ac = self.asv.get_all_accounts()
        if all_ac == None or len(all_ac) == 0:
            print('등록된 계좌가 없습니다.')
        else:
            for i in range(len(all_ac)):
                print(all_ac[i])

    def menu_list_member_accounts(self):
        print('\n[ 회원별 계좌 목록 ]')
        mid = input('조회할 회원 ID : ')
        ac_list = self.asv.get_members_accounts(mid)
        if ac_list == None or len(ac_list) == 0:
            print('해당 회원의 계좌가 없습니다.')
        else:
            for i in range(len(ac_list)):
                print(ac_list[i])

    def run_admin_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_member_menu)
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
        if m_list == None or len(m_list) == 0:
            print('등록된 회원이 없습니다.')
        else:
            for i in range(len(m_list)):
                print(m_list[i])

    def menu_view_member_info(self):
        print('\n[ 회원 정보 조회 ]')
        mid = input('조회할 회원 ID : ')
        member = self.msv.view_member_info(mid)
        if member:
            print(member)
        else:
            print('없는 id입니다.')

    def menu_delete_member(self):
        print('\n[ 회원 강퇴 ]')
        del_id = input('강퇴할 회원 ID : ')
        if self.msv.remove_member(del_id):
            print('회원을 삭제하였습니다.')
        else:
            print('회원 삭제에 실패하였습니다.')

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()