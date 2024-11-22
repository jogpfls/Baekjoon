T = int(input())
result = []
for _ in range(T):
  VPS = list(input())
  if len(VPS)%2 != 0:
    result.append("NO")
  else:
    for _ in range(int(len(VPS)/2)):
      for i in range(len(VPS)-1):
        if VPS[i] == "(" and VPS[i+1] == ")":
          VPS[i] = "*"
          VPS[i+1] = "*"

      for i in range(VPS.count("*")):
        VPS.remove("*")
      
      if len(VPS) == 0:
        result.append("YES")
        break
    if len(VPS) != 0:
      result.append("NO")

        
for value in result:
  print(value)

