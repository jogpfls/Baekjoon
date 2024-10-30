A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
array = [0 for _ in range(10)]

for i in range (len(result)):
  array[int(result[i])] += 1

for i in array:
  print(i)