import random

# 1. 컴퓨터가 숫자를 생각한다(1-50)
N = random.randint(1, 50) 

# 5. 7번 반복 (시험 범위의 제어문 구조 참고)
for i in range(1, 8):
    # 2. 사용자 숫자를 입력받음
    guess = int(input(f"[{i}회차] 숫자입력: "))

    # 3. 숫자가 맞으면 사용자 win
    if guess == N:
        print("Win")
        break 
    
    # 4. 틀리면 UP/DOWN 힌트 제공
    elif guess < N:
        print("UP")
    else:
        print("DOWN")

# 6. 7번 내에 break(정답)를 못 만났을 경우 실행되는 블록
else:
    print(f"Computer Win!")