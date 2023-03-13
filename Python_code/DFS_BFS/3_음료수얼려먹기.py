# 혼자서 못 풀어서 답지 봄

n, m = map(int, input().split())

# 2차원 리스트 입력값 받는 방법 (NxM)
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

##### 입력 받는 법 익히기 ! #####

def dfs(x,y):
  # 범위 밖이면 즉시 종료
  if x <= -1 or x >= n or y <= -1 or y>= m:
    return False
  if graph[x][y] == 0:
    # 방문처리 1로 바꾸기
    graph[x][y] == 1
    # 상하좌우 재귀적으로 호출
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  # 0이 아니면 
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1
  
print(result)