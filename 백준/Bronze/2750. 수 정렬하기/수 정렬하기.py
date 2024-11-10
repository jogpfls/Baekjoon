array = []
N = int(input())
for i in range(N):
  array.append(int(input()))

array = sorted(array)

for value in array:
  print(value)