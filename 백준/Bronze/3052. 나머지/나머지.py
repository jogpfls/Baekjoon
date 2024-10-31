array = []
count = 0

for i in range(10):
  N = int(input())
  array.append(N%42)

unique_remainders = set(array)
count = len(unique_remainders)

print(count)
