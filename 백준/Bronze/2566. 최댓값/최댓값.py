result = []
for _ in range(9):
  n = list(map(int, input().split()))
  result.append(n)
r = 0
num1 = 0
num2 = 0

for i in range(9):
  for j in range(9):
    if result[i][j] >= r:
      r = result[i][j]
      num1 = i+1
      num2 = j+1


print(r)
print(num1, num2)

