arr = list(map(int, input().split()))
set = set(arr)

if len(set) == 3:
    print(max(arr) * 100)
elif len(set) == 2:
    for i in range(3):
        if arr.count(arr[i]) == 2:
            print(1000+arr[i]*100)
            break
elif len(set) == 1:
    print(10000 + arr[0] * 1000)