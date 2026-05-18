from account.account import AccountService
        
def select_manu():
    print("===============================================")
    print('1.계좌생성 | 2.계좌목록 | 3.입금 | 4.출금 | 0.종료')
    print("===============================================")
    menu = int(input('>> 메뉴선택 : '))
    return menu

aservice = AccountService()
def start_console_bank(aservice):
    print()
    print('=================Euijin Bank==================')
    while True:
        menu = select_manu()
        if menu == 0: break
        elif menu == 1:
            account_no = input("> 계좌번호 : ")
            owner = input("> 계좌주 : ")
            balance = int(input("> 초기 입금액 : "))
            if aservice.create_account(account_no,owner,balance):
                print('계좌가 생성되었습니다')
        elif menu == 2:
            list_account = aservice.get_list_account()
            print('=============')
            print('===계좌목록===')
            print('=============')
            for account in list_account:
                print(account)
        elif menu == 3:
            print('=============')
            print('=====예금====')
            print('=============')
            account_no = input('> 계좌번호')
            amount = int(input('> 예금액 : '))
            aservice.deposit(account_no, amount)
            print(f"{amount}원이 입금되었습니다")
        elif menu == 4:
            print('=============')
            print('=====출금====')
            print('=============')
            account_no = input('> 계좌번호')
            amount = int(input('> 출금액 : '))
            aservice.deposit(account_no, amount)
            print(f"{amount}원이 출금되었습니다")

    print('=============이용해주셔서 감사합니다============')

if __name__ == '__main__':
    aservis = AccountService()
    start_console_bank(aservis)