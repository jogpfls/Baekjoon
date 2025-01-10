K, M = map(int, input().split())
lan = [int(input()) for _ in range(K)]

#이분탐색 처음과 끝
start, end = 1, max(lan)

while start <= end:
  mid = (start+end)//2 #중간 위치
  lines = 0 #랜선 수
  for i in lan:
    lines += i//mid #랜선의 갯수 찾기

  if lines >= M:
    start = mid +1
  else:
    end = mid - 1

print(end)