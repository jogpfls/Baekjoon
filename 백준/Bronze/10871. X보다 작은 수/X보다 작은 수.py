N, X = map(int, input().split())

array = list(map(int, input().split()))
resultArray = []

for i in range(0, N) :
  if(array[i] < X) :
    resultArray.append(array[i])

print(*resultArray)