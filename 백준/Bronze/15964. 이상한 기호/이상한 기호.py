def sum(num1, num2):
	return (num1+num2)*(num1-num2)

A, B = map(int, input().split())

print(sum(A, B))