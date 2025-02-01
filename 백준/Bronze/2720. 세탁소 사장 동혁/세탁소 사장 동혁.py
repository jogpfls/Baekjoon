T = int(input())

for _ in range(T):
    C = int(input())
    money = []
    money.append(C//25)
    C -= C//25*25
    money.append(C//10)
    C -= C//10*10
    money.append(C//5)
    C -= C//5*5
    money.append(C)
    print(*money)