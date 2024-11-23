import sys
input = sys.stdin.readline

N = int(input())
arrayN = set(map(int, input().split()))
M = int(input())
arrayM = list(map(int, input().split()))

for value in arrayM:
  if value in arrayN:
    print(1)
  else:
    print(0)