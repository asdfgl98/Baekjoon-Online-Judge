n = int(input())

arr = []
result = []
for _ in range(n):
  c = int(input())
  arr.append(c)

for i in arr:
  q = i//25
  d = (i%25)//10
  n = (i%25%10)//5
  p = (i%25%10%5)//1
  result.append([int(q),int(d),int(n),int(p)])

for i in result:
  for j in range(len(i)):
    print(i[j], end=' ')
  print('')

