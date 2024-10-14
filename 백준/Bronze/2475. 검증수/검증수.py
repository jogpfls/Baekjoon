def sum(A, B, C, D, E):
	return (A*A + B*B + C*C + D*D + E*E) % 10

num1, num2, num3, num4, num5 = map(int, input().split())

print(sum(num1, num2, num3, num4, num5))