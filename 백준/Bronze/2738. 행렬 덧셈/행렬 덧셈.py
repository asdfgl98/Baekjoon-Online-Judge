n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
  w = list(map(int, input().split()))
  a.append(w)

for i in range(n):
  w = list(map(int, input().split()))
  b.append(w)



for i in range(n):
  for j in range(m):
    a[i][j] += b[i][j]
    print(a[i][j], end=' ')
  print('')