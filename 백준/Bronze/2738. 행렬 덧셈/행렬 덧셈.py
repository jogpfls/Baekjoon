N, M = map(int, input().split())

array1=[]
array2 = []

for i in range(N):
	array1.append(list(map(int, input().split())))

for i in range(N):
	array2.append(list(map(int, input().split())))

result = array1
for i in range(0, N):
	for j in range(0, M):
		result[i][j] = (array1[i][j] + array2[i][j])
		
for i in range(N):
  print(*result[i])	
