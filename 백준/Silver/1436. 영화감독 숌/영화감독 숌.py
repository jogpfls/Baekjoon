N = int(input())

count = 0

while(True):
  count += 1
  if "666" in str(count):
    N -= 1
  if N == 0:
    break

print(count)
