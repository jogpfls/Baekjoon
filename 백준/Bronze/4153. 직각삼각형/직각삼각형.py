import sys
input = sys.stdin.readline

while(True):
  array = list(map(int, input().split()))
  if array[0] ==0 and array[1] ==0 and array[2] == 0:
    break
  maxValue = max(array)
  array.remove(maxValue)
  if array[0]**2 + array[1]**2 == maxValue**2:
    print("right")
  else:
    print("wrong")