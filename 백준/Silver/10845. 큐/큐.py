import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
  cmd = input().split()
  if cmd[0] == "push":
    array.append(cmd[1])
  elif cmd[0] == "pop":
    if len(array) == 0:
      print(-1)
    else:
      print(array.pop(0))
  elif cmd[0] == "size":
    print(len(array))
  elif cmd[0] == "empty":
    if len(array) == 0:
      print(1)
    else:
      print(0)
  elif cmd[0] == "front":
    if len(array) == 0:
      print(-1)
    else:
      print(array[0])
  elif cmd[0] == "back":
    if len(array) == 0:
      print(-1)
    else:
      print(array[-1])