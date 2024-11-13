
C = int(input())
percentage = []

for i in range(C):
  count = 0
  array = list(map(int, input().split()))
  average = (sum(array[1:]))/(array[0])

  for j in range(1, len(array)):
    if array[j] > average:
      count += 1

  percentage.append((count/array[0])*100)


for value in percentage:
  print(f"{value:.3f}%")