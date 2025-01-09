import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [list(map(int, input().split())) for i in range(N)]

up = N*M

left = 0
for i in range(N):
  for j in range(M):
    if j == 0:
      left += array[i][j]
    else:
      if array[i][j-1] < array[i][j]:
        left += array[i][j] - array[i][j-1]

right = 0
for j in range(M):
  for i in range(N):
    if i == 0:
      right += array[i][j]
    else:
      if array[i-1][j] < array[i][j]:
        right += array[i][j] - array[i-1][j]

print(2*(up + left + right))