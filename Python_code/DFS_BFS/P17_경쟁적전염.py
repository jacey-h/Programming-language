# ##### 입력 받기 ######
# n, k = map(int, input().split())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int,input().split())))

# s, result_x, result_y = map(int, input().split())

# ###### 시작
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# temp = [[0]*n for _ in range(n)]

# for i in range(s): # s초 동안
#   for v in range(k,0,-1):
#     for x in range(n):
#       for y in range(n):    
#         if graph[x][y] == v:
#           for j in range(4):
#             nx = x + dx[j]
#             ny = y + dy[j]
        
#             if 0 <= nx < n and 0 <= ny < n:
#               if graph[nx][ny] == 0 or graph[nx][ny] > v:
#                 temp[nx][ny] = v
#   for x in range(n):
#     for y in range(n):
#       if graph[x][y] == 0 and graph[x][y] != temp[x][y]:
#         graph[x][y] = temp[x][y] 
        
# print(graph[result_x-1][result_y-1])

##### 정답 #######
from collections import deque

n, k = map(int, input().split())
graph = []
data = []
for i in range(n):
  graph.append(list(map(int,input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      data.append((graph[i][j],0,i,j))

data.sort()
q = deque(data)

result_s, result_x, result_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
  virus, s, x, y = q.popleft()
  if s == result_s:
    break
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
      
    if 0 <= nx < n and 0 <= ny < n:
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus,s+1,nx,ny))
        
print(graph[result_x-1][result_y-1])
