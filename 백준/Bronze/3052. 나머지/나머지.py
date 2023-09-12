n = []
for i in range(1,11):
  a = int(input())
  n.append(a%42)

print(len(set(n)))