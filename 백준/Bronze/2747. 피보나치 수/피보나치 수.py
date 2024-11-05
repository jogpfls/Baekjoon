import sys
n = int(sys.stdin.readline())
result = 0
for i in range(n):
  if i == 0:
    a = 0
    b = 1
  a = b
  b = result

  result = a+b

print(result)
