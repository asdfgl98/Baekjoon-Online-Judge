z = int(input())
for i in range(1, z+1):
  print(' '*(z-i)+"*"*(i*2-1))
for j in range(z-1,0,-1):
  print(' '*(z-j)+"*"*(j*2-1))