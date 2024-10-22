a = int(input())
arr = []
for i in range(a):
  line = []
  b, c = input().split()
  b = int(b)

  for j in range(len(c)):
    line.append(c[j]*b)

  arr.append(line)

for i in range(len(arr)):
  for j in range(len(arr[i])):
    print(arr[i][j], end ="")
  print()