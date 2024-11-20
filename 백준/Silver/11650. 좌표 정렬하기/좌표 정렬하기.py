N = int(input())
array = []
for _ in range(N):
  array.append(list(map(int, input().split())))

array = sorted(array)

for value in array:
  print(*value)
