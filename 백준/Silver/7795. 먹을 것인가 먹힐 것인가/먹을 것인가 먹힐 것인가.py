T = int(input())

#이분 탐색 함수
def binary_search(arr, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1
    return start #num보다 작은 값의 개수를 반환

for j in range(T):
    result = 0
    M_A, M_B = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort() #이분탐색을 위한 정렬
    for i in range(len(A)):
        result += binary_search(B, A[i])
    print(result)