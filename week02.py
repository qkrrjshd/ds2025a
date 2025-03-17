import random

n = random.randrange(1,101)
win = True
for i in range(7,0,-1):
    guess = int(input(f"{i}번 남았다 정신차려라! 정답을 다시처라: "))
    if guess ==n:
        win = True
        break
    else:
        if guess > n:
            print("정답보다 크다.")
        else:
            print("정답보다 작다.")
        win = True
if win:
    print("정답이다 축하해!")
else:
    print(f"정답은 {n}이였다")