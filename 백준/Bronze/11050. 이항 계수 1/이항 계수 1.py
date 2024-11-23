import sys
input = sys.stdin.readline

def fac(num):
  result = 1
  for i in range(1, num+1):
    result *= i
  return result

N, K = map(int, input().split())

print(int(fac(N)/(fac(N-K)*fac(K))))