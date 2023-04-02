########## 입력받기 ###########
n = int(input())
# 맵정보
array = [[0]*(n+1) for _ in range(n+1)]

k = int(input())
for _ in range(k):
  x,y = map(int,input().split())
  array[x][y] = 1
# 방향회전 정보
info = [] 
l = int(input())
for _ in range(l):
  x,c = input().split()
  info.append((int(x),c))
  
############# 방향 ###############
dx = [0,1,0,-1] #  보는 방향 동,남,서,북
dy = [1,0,-1,0]

def turn(direction, c):
  if c == 'L':
    direction = (direction-1)%4
  else:
    direction = (direction+1)%4
  return direction

########### 시뮬레이션 시작 #########
def simulate():
  x,y =1,1
  array[x][y] = 2 # 뱀이 존재하는 위치
  direction = 0
  time = 0
  index = 0 # 다음에 회전할 정보
  q = [(x,y)] # 뱀이 차지하고 있는 위치 / 꼬리가 앞쪽 
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]
  
    # if nx < 1 or nx > n or ny < 1 or ny > n or array[nx][ny] == 2 :
    if nx >= 1 and  nx <= n and ny >= 1 and ny <= n and array[nx][ny] != 2 :
      if array[nx][ny] == 0 :
        array[nx][ny] = 2
        q.append((nx,ny)) # 이 생각못함
        px,py = q.pop(0)
        array[px][py] = 0
      if array[nx][ny] == 1 :
        array[nx][ny] = 2
        q.append((nx,ny))
    else:
      time += 1
      break
    x,y = nx,ny
    #print(f' x,y : {x,y}')
    time += 1
    #print(f'time : {time}')
    if index < l and time == info[index][0]: # 이부분도 생각못함
      #print(f'index: {index}')
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())
