import sys

N = int(sys.stdin.readline().strip())

a = []

for i in range(0, N):
  A, B = map(int, sys.stdin.readline().strip().split())
  a.append(A + B)

for i in range(0, N):
  print(a[i])