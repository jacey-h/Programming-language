''' 내가 처음 푼거
n= int(input())
plan = list(input().split()) #알아서 리스트로 만들어줌
print(plan)
x=1
y=1
for i in range(len(plan)):

  if plan[i] == 'L':
    y-=1
    if y<1:
      y+=1   
  elif plan[i] == 'R':
    y+=1
    if y>n:
      y-=1
  elif plan[i] == 'U':
    x-=1
    if x<1:
      x+=1
  elif plan[i] == 'D':
    x+=1
    if x>n:
      x-=1
print(x,y)
'''

# 정답

n = int(input())
x,y = 1,1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:

  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

    if nx<1 or nx>n or ny<1 or ny>n:
      continue
    x, y = nx, ny

print(x,y)