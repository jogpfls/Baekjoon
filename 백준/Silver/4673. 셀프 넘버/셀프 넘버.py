number = [x for x in range(1, 10000)]

for i in range(1, 10000):
  result = list(map(int, str(i)))
  resultCount = i
  resultCount = resultCount + sum(result)
  if resultCount not in number:
    continue
  else:
    number.remove(resultCount)

for value in number:
  print(value)