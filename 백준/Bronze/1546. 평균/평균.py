N = int(input())

array = list(map(int, input().split()))

M = max(array)

for i in range(N):
  array[i] = array[i]/M*100

print(sum(array)/N)