import random

words = ['ska', 'gy', 'tjd', 'qwer', 'wasd']
target = random.choice(words).upper()
display = ['_'] * len(target)
chances = 7
history = []

print("시작")

while chances > 0:
    print(f"\n상태: {' '.join(display)} (남은 기회: {chances})")
    guess = input(">> 알파벳 입력: ").upper()

    if guess in history:
        print("이미 입력한 알파벳입니다.")
        continue
    
    history.append(guess)

    if guess in target:
        for idx, char in enumerate(target):
            if char == guess:
                display[idx] = guess
    else:
        chances -= 1
        print(f"오답")

    if '_' not in display:
        print(f"\정답: {target}")
        print("Win")
        break

if chances == 0:
    print(f"\n정답은 {target}이었습니다.")
    print("Loose")