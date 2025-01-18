T = int(input())

#이진 탐색 함수
def binary_search(array, num):
	start = 0
	end = len(array)-1

	while start <= end:
		mid = (start + end) // 2
		if num == array[mid]: #값이 일치하면 True 변환
			return True 
		elif num < array[mid]: # 탐색 범위 축소 (왼쪽 절반)
			end = mid-1
		elif num > array[mid]: # 탐색 범위 축소 (오른쪽 절반)
			start = mid+1 #값을 찾지 못하면 False 반환
	
	return False

for _ in range(T):
    # 입력 받기
	N_1 = int(input())
	arr_1 = list(map(int, input().split()))
	N_2 = int(input())
	arr_2 = list(map(int, input().split()))

	#arr_1 배열을 이진탐색하기 위해 정렬
	arr_1.sort()	

	for i in range(N_2):
		if binary_search(arr_1, arr_2[i]):
			print(1)
		else:
			print(0)