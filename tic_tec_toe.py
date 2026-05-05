



# 1. 자료구조
# 화면에 보여줄 보드
board_screen = ' 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8'

board = [" "] * 9 # 게임의 진행 상태
board_blank = set(range(9))     # 빈 set 자료형태  0~8까지 생성
# 이겼을 때의 상태
win_status = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
              (0, 3, 6), (1, 4, 7), (2, 5, 8),
              (0, 4, 8), (2, 4, 6)]
human = 'O'
computer = 'X'

# 2. 필요한 함수 정의
def showBoard():
    print(board_screen)

def updateGame(who, number):
    global board, board_screen
    board[number] = who
    board_screen = board_screen.replace(str(number), who)
    board_blank.discard(number)


# random표준 라이브러리 사용
import random
def getComputerNumber():
    if board_blank:
        # return board_blank.pop()    # 빈 칸 있으면 아무거나 하나 넘김
        return random.choice(list(board_blank))
    return -1

def isWin(turn):
    for status in win_status:
        if board[status[0]] == board[status[1]] == board[status[2]] == turn:
            return True
    return False


# 3. 메인 로직
# 3-1. 필요한 자료구조 초기화
print('Tic-Tac-Toe')
# 3-2. 보드를 보여줌
showBoard()
while True:
    # 3-3. human 차례
    # human 입력 받아서 처리
    human_input = int(input(' >> 숫자를 입력하세요 : '))
    updateGame(human, human_input)
    showBoard()
    if isWin(human):
        print('You Win !')
        break

    # 3-4. 컴퓨터 차례
    # computer가 놓을 자리를 선택
    computer_input = getComputerNumber()
    if computer_input == -1:
        print('비김')
        break
    updateGame(computer, computer_input)
    print(' >> 컴퓨터 : ', computer_input)
    showBoard()
    if isWin(computer):
        print('looser')
        break
