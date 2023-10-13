result = []
count = 0


for i in range(5):
  t = input()
  result.append(t)
  if len(t) > count:
    count = len(t)

for i in range(count):
  
    for j in range(5):
      try:
        print(result[j][i], end='')
      except:
        continue
    

      