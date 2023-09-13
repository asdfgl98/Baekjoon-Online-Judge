ch = [1,1,2,2,2,8]
result = []
x = input().split()
x = list(map(int, x))

for i in range(len(ch)):
  result.append(ch[i]-x[i])

for i in result:
  print(i, end=' ')