import sys
input = sys.stdin.readline

N = int(input())
card = sorted(list(map(int, input().split())))

M = int(input())
MCard = list(map(int, input().split()))

dic1 = {}
for x in card:
  if x in dic1:
    dic1[x] += 1
  else:
    dic1[x] = 1

for i in MCard:
  if i in dic1:
    print(dic1[i], end=" ")
  else:
    print(0, end=" ")