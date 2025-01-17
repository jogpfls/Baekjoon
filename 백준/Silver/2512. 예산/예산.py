N = int(input())
arr = list(map(int, input().split()))
allMoney = int(input())

#파이썬 sort 함수의 시간복잡도는 최적화가 잘 된 nlogn
arr.sort()

#이진 탐색을 통해 상한값 찾기
start = 0
end = arr[-1]
result = 0

while start <= end:
	total = 0
	mid = (start + end) // 2
	
	#상한값이 mid일 때
	for num in arr:
		if num <= mid:
			total += num
		else:
			total += mid
	
	if total <= allMoney:
		result  = mid
		start = mid + 1
	else:
		end = mid - 1

print(result)