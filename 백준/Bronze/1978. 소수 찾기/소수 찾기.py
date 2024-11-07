import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
delete = []

for i in range(N):
  if array[i] == 1:
    delete.append(array[i])
  for j in range(1, array[i]+1):
    if j != 1 and j != array[i]:
      if array[i]%(j) == 0:
        delete.append(array[i])
        break

print(len(array)-len(delete))