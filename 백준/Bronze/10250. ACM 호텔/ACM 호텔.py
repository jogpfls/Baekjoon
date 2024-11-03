T = int(input())
a = []
for i in range(T):
  H, W, N = map(int, input().split())
  
  floor = N%H
  if floor == 0:
    floor = H
  room_number = (N - 1) // H + 1
  a.append(f"{floor}{room_number:02}")

for room in a:
    print(room)