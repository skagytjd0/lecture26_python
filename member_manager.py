class Member:
    def __init__(self, user_no, id, pw, name, phone, adress):
        self.__user_no = user_no
        self.__id = id
        self.__pw = pw
        self.__name = name
        self.__phone = phone
        self.__adress = adress

    def __str__(self):
        return f'\n회원번호: {self.__user_no}\n아이디: {self.__id}\t비밀번호: {self.__pw}\n회원명: {self.__name}\n전화번호: {self.__phone}\n주소: {self.__adress}\n-----------------------------------------'

    def update_member(self, name, pw, phone, adress):
        self.__name = name
        self.__pw = pw
        self.__phone = phone
        self.__adress = adress

    def get_user_no(self):
        return self.__user_no
    
    def get_id(self):
        return self.__id
    
    def get_pw(self):
        return self.__pw

class MemberService:
    def __init__(self):
        self.__member_list = []

    def create_member(self, user_no, id, pw, name, phone, adress):
        member = Member(user_no, id, pw, name, phone, adress)
        self.__member_list.append(member)
        return True

    def list_member(self):
        return self.__member_list

    def info_member(self, user_no):
        for member in self.__member_list:
            if member.get_user_no() == user_no:
                return member
        return None

    def corr_member(self, user_no, name, pw, phone, adress):
        member = self.info_member(user_no)
        if member:
            member.update_member(name, pw, phone, adress)
            return True
        return False

    def delete_member(self, user_no, id, pw):
        for i in range(len(self.__member_list)):
            member = self.__member_list[i]
            if member.get_user_no() == user_no and member.get_id() == id and member.get_pw() == pw:
                self.__member_list.pop(i)
                return True
        return False

memservice = MemberService()

while True:
    print('\n===== 회원 관리 프로그램 =====')
    print('1. 회원가입 | 2. 목록조회 | 3. 상세조회 | 4. 정보수정 | 5. 회원탈퇴 | 0. 종료')
    
    try:
        menu_input = input('>> 메뉴선택 : ')
        menu = int(menu_input)
    except ValueError:
        print('! 오류: 숫자를 입력해주세요.')
        continue

    if menu == 0:
        print('프로그램을 종료합니다.')
        break

    elif menu == 1:
        try:
            user_no = int(input('> 회원번호 : '))
            id = input('> 아이디 : ')
            pw = input('> 비밀번호 : ')
            name = input('> 이름 : ')
            phone = input('> 전화번호 : ')
            adress = input('> 주소 : ')
            memservice.create_member(user_no, id, pw, name, phone, adress)
            print('결과 : 회원가입 성공!')
        except ValueError:
            print('! 오류: 회원번호는 숫자로 입력해야 합니다.')

    elif menu == 2:
        member_list = memservice.list_member()
        if not member_list:
            print('등록된 회원이 없습니다.')
        else:
            for member in member_list:
                print(member)

    elif menu == 3:
        try:
            user_no = int(input('> 조회할 회원번호 : '))
            member = memservice.info_member(user_no)
            if member:
                print(member)
            else:
                print('결과 : 해당 회원정보가 없습니다.')
        except ValueError:
            print('! 오류: 숫자를 입력하세요.')

    elif menu == 4:
        try:
            user_no = int(input('> 수정할 회원번호 : '))
            member = memservice.info_member(user_no)
            if member:
                name = input('> 새 이름 : ')
                pw = input('> 새 비밀번호 : ')
                phone = input('> 새 전화번호 : ')
                adress = input('> 새 주소 : ')
                if memservice.corr_member(user_no, name, pw, phone, adress):
                    print('결과 : 수정 완료')
            else:
                print('결과 : 수정할 회원이 없습니다.')
        except ValueError:
            print('! 오류: 숫자를 입력하세요.')

    elif menu == 5:
        try:
            print('[본인 확인 절차]')
            user_no = int(input('> 탈퇴할 회원번호 : '))
            input_id = input('> 아이디 확인 : ')
            input_pw = input('> 비밀번호 확인 : ')
            
            if memservice.delete_member(user_no, input_id, input_pw):
                print('결과 : 회원 탈퇴가 성공적으로 처리되었습니다.')
            else:
                print('결과 : 입력 정보가 일치하지 않아 탈퇴가 불가능합니다.')
        except ValueError:
            print('! 오류: 회원번호는 숫자로 입력하세요.')
    
    else:
        print('잘못된 메뉴 선택입니다.')