from collections import deque

N = int(input())

card = deque(i+1 for i in range(N))

for i in range(N-1):
  card.popleft()
  card.append(card[0])
  card.popleft()

print(*card)
