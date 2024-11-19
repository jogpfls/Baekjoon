N = int(input())

first = 0
second = 1
result = 0

if N == 1 or N ==2:
    print(1)
else:
    for _ in range(N-1):
        result = first + second
        first = second
        second = result

    print(result)
