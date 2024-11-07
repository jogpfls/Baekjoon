import sys

result = []
T = int(sys.stdin.readline())
for i in range(T):
  a, b = map(int, sys.stdin.readline().split())
  a = a%10

  if a == 0:
    result.append(10)
  
  elif a == 1 or a == 5 or a == 6:
    result.append(a)
  
  elif a == 4 or a == 9:
    if b%2 == 0:
      result.append((a**2)%10)
    else:
      result.append(a)

  else:
    if b%4 == 0:
      result.append((a**4)%10)
    else:
      result.append((a**(b%4))%10)

for value in result:
  print(value)

  
