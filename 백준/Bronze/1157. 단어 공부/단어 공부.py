x = input().lower()
x_list = list(set(x))
result = []

for i in x_list:
  result.append(x.count(i))

m = max(result)
r = result.count(m)
if r >= 2:
  print('?')
else:
  print(x_list[result.index(m)].upper())
