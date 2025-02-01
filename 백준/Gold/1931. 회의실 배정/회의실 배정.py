n = int(input())
time = [] # n개의 회의 정보를 저장할 리스트
result = [] # 선택된 회의를 저장할 리스트

for i in range(n):
    time.append(list(map(int, input().split())))

#끝나는 시간을 기준으로 정렬
time.sort(key=lambda x: (x[1], x[0]))
result.append(time[0]) #첫 번째 회의를 결과 리스트에 추가

for i in range(1, len(time)):
    if time[i][0] >= result[-1][1]: # 이전 회의가 끝난 후 시작하는 회의 선택
        result.append(time[i]) # 선택한 회의를 결과 리스트에 추가

print(len(result))