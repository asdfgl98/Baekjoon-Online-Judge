n = int(input())
cnt = n

for i in range(n):    
  d = input()
  for j in range(0, len(d)-1):
    if d[j] == d[j+1]:
      pass
    elif d[j] in d[j+1:]:
      cnt -= 1
      break

print(cnt)