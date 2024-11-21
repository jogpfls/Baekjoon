N = int(input())
result = []
for _ in range(N):
  array = []
  k = int(input())
  n = int(input())

  for i in range(0, k+1):
    zero = []
    remain = []
    for j in range(n):
      if i == 0:
        zero.append(j+1)
      else:
        remain.append(sum(array[i-1][:j+1]))
    if i == 0:
      array.append(zero)
    else:
      array.append(remain)

  result.append(array[-1][-1])

for value in result:
  print(value)
