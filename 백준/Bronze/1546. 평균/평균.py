n = int(input())
result = []

def x(x,y):
  result.append(x/y*100)

n1 = input().split()
n1 = list(map(int, n1))

for i in range(n):
  x(n1[i], max(n1))
print(sum(result)/len(result))