import random

# 1. 단어 리스트 (자료에 나온 방식대로 소문자로 구성하거나, 
# 처음부터 대문자로 적어두는 것이 .upper()를 피하는 방법입니다.)
words = ['SKA', 'GY', 'TJD', 'QWER', 'WASD']
target = random.choice(words)

# 2. 표시용 리스트 생성
display = ['_'] * len(target)
chances = 7
history = []

print("시작")

while chances > 0:
    print("\n상태: ", end="")
    for char in display:
        print(char, end=" ")
    print(f"(남은 기회: {chances})")

    guess = input(">> 알파벳 입력 (대문자): ")

    if guess in history:
        print("이미 입력한 알파벳입니다.")
        continue
    
    history.append(guess)

    if guess in target:
        for i in range(len(target)):
            if target[i] == guess:
                display[i] = guess
    else:
        chances -= 1
        print("오답")

    if '_' not in display:
        print(f"\n정답: {target}")
        print("Win")
        break

if chances == 0:
    print(f"\n정답은 {target}이었습니다.")
    print("Loose")
