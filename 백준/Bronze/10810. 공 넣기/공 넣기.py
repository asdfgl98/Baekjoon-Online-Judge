n,m = input().split()
n = int(n)
m = int(m)

ba = {}

i = 0
j = 0
k = 0

for i in range(1,n+1):
  ba[i] = 0

for _ in range(1,m+1):
  i,j,k = input().split()
  i = int(i)
  j = int(j)
  k = int(k)
  for i in range(i,j+1):
    ba[i] = k

for i in range(1, n+1):
  print(ba[i], end = ' ')