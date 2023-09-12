n, m = map(int, input().split())
ba =[]
for i in range(1, n+1):
  ba.append(i)
newr = 0

for i in range(m):
  i, j = map(int, input().split())
  temp = ba[i-1:j]
  temp.reverse()
  ba[i-1:j] = temp

for i in range(n):
  print(ba[i], end=' ')
  
  