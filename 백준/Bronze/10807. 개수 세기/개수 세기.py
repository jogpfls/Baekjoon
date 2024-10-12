N = int(input())
array = list(map(int, input().split()))
V = int(input())
number = 0

for i in range(0, N):
  if(array[i] == V) :
    number = number +1

print(number)