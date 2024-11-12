N = int(input())
count = 0

array = []
if N < 10:
  array.append(0)
  array.append(N)
else:
  array.append(str(N)[0])
  array.append(str(N)[1])

first = int(array[0])
last = int(array[1])

while(1):
  result = first + last
  count += 1
  if result < 10:
    first = last
    last = result
  else:
    first = last
    last = int(str(result)[1])
  
  if first*10 + last == N :
    break

print(count)

