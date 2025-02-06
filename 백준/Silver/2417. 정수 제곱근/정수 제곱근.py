import math

n = int(input())
q = math.isqrt(n)

if q * q < n:
    q += 1

print(q)