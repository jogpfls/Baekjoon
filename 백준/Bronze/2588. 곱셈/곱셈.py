import sys

a = int(sys.stdin.readline())
b = sys.stdin.readline()

result = []
total = 0

for i in range(len(b)-1):
  gob = a*int(b[len(b)-2-i])
  result.append(gob)
  total += (10**i)*gob
  print(result[i])

print(total)

