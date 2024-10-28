N = int(input())
total = 0
array = []
for i in range(N):
  array.append(list(input()))

for i in range(N):
  number = 0
  for j in range(len(array[i])):
    if array[i][j] == 'X':
      number = 0
    else:
      number += 1
      total += number

  print(total)
  total = 0
