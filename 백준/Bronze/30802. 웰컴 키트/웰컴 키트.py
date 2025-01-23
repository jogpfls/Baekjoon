N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
count = 0
for i in range(len(size)):
    if size[i] == 0:
        continue
    elif size[i] <= T:
            count += 1
    elif size[i] % T == 0:
        count += size[i]//T
    else:
        count += size[i]//T+1

p_count = N//P
pen = N%P

print(count)
print(f"{p_count} {pen}")