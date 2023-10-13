grade_list = ["A+", "A0", "B+", "B0", "C+", "C0", "D+", "D0", "F"]
score_list = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
h = 0
y = 0

for _ in range(20):
  s,p, g = input().split()
  if g != 'P':
      h += float(p) * float(score_list[grade_list.index(g)])
      y += float(p)

print(round(h/y, 6))

