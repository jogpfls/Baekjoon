import sys
T = int(sys.stdin.readline())
result = []

for _ in range(T):
  array = sys.stdin.readline().split()
  
  if array[0] == 'push':
    result.append(array[1])
  elif array[0] == "pop":
    if len(result) == 0:
      print(-1)
    else:
      print(result.pop())
  elif array[0] == "size":
    print(len(result))
  elif array[0] == "empty":
    if len(result) == 0:
      print(1)
    else:
      print(0)
  elif array[0] == "top":
    if len(result) == 0:
      print(-1)
    else:
      print(result[-1])