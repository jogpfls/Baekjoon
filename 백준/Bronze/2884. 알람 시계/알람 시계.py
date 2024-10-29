H, M = map(int, input().split())

if(H == 0 and M < 45):
  H = 24
newH = ((H*60)+M - 45)//60
newM = ((H*60)+M - 45)%60

print(newH, newM)