import sys
input = sys.stdin.readline

N = int(input())
array = []
for _ in range(N):
  array.append(int(input()))

for value in sorted(array):
  print(value)