array = list(map(int, input().split()))

if array == list(range(1, 9)):
  print("ascending")

elif array == list(range(8, 0, -1)):
  print("descending")

else:
  print("mixed")
