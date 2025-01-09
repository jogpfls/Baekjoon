N, M = map(int, input().split())

array = [input() for _ in range(N)]
count = []

for a in range(N-7):
  for b in range(M-7):
    index1 = 0 #왼쪽 위가 B로 시작할 때
    index2 = 0 #왼쪽 위가 W로 시작할 때
    for i in range(a, a+8):
      for j in range(b, b+8):

        if (i+j)%2 == 0:
          if array[i][j] == "B":
            index2 += 1
          else:
            index1 += 1
        else:
          if array[i][j] == "B":
            index1 += 1
          else:
            index2 += 1
    count.append(min(index1, index2))

print(min(count))