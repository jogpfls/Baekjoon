import sys
input = sys.stdin.readline

N = int(input())

array = [input().split() for _ in range(N)]
array.sort(key=lambda array: int(array[0]))

for value in array:
  print(*value)