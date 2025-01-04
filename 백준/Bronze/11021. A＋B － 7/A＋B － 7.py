N = int(input())
array = []
for _ in range(N):
  A, B = map(int, input().split())
  array.append(A+B)

for i in range(len(array)):
  print(f"Case #{i+1}: {array[i]}")