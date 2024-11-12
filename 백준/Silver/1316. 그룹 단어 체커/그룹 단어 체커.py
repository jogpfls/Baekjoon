N = int(input())
count = 0
for i in range(N):
  array = list(input())
  setArray = set(array)

  for j in range(len(array)):
    if array[j] in setArray:
      if j < len(array)-1:
        if array[j] == array[j+1]:
          continue
        else:
          setArray.remove(array[j])
      elif j == len(array)-1:
        if array[j] not in setArray:
          count += 1
          break
    else:
      count += 1
      break

print(N - count)