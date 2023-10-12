x = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in cro:
  cnt = cnt + x.count(i)
  x = x.replace(i, " ")

x = x.replace(" ", "")
cnt += len(x)
print(cnt)