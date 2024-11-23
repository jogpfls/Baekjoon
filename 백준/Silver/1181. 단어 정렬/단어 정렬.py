N = int(input())
array = [[] for _ in range(50)]

for _ in range(N):
  text = input()
  if text in array[len(text)-1]:
    continue
  else:
    array[len(text)-1].append(text)
    array[len(text)-1] = sorted(array[len(text)-1])

for i in range(50):
  if len(array[i]) != 0:
    for value in array[i]:
      print(value)