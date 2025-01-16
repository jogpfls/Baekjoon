N, K = map(int, input().split()) #N과 K입력 저장
arr = [i for i in range(1, N+1)] #1부터 N까지 수 저장
i = 0 #K를 담을 i 변수
result = [] #결과를 담을 리스트 변수

while(True): #반복문 구현
	if len(arr) == 0: #모든 사람이 제거됬을 때 반복문 탈출
		break

	i += K #K번째

	if i <= N: #제거해야할 순서의 사람이 N보다 작을 때
		result.append(arr[i-1]) #결과값 저장
		arr[i-1] = 0 #배열 숫자가 밀리지 않도록 삭제하기 전에 아무숫자로 일단 지정
	else:
		i = i-N-K
		arr = [x for x in arr if x!= 0] #배열 안에 있는 모든 0(아무숫자) 삭제
	
	N = len(arr) # N의 크기 다시 지정

print(f"<{', '.join(map(str, result))}>")