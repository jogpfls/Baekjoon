import sys

a, b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())

min = (a * 60) + b + c
print(min//60-24 if min//60 >=24 else min//60, min-(min//60)*60)