import random

words = ['SKA', 'GY', 'TJD', 'QWER', 'WASD']
target = random.choice(words)

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
