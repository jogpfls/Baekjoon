M, D = map(int, input().split())
count = D
Day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if M == 1:
  print(Day[count%7])

else:
  for i in range(1, M):
    if i == 4 or i == 6 or i == 9 or i == 11:
      count += 30
    elif i == 2:
      count += 28
    else:
      count += 31
  print(Day[count%7])

