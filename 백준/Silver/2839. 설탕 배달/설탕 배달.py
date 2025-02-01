N = int(input())
cnt = 0

while True:
    if N % 5 != 0:
        N -= 3 
        cnt += 1
    elif N % 5 == 0:
        cnt += N // 5
        print(cnt)
        break
    if N < 0:
        print(-1)
        break