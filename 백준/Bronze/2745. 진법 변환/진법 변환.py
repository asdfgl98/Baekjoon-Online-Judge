n, b = input().split()
n = ''.join(reversed(n))
b = int(b)
z = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0
for i in range(len(n)-1,-1,-1):
  result += b**i * z.index(n[i])
print(result)