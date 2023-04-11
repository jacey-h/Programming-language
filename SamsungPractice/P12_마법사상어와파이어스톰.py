import copy
from collections import deque

num, q = map(int,input().split())
n = 2**num
array = [list(map(int,input().split())) for _ in range(n)]
l = list(map(int,input().split()))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 90도 시계방향 회전
def rot90(m,arr):
    new_arr = [[0]*m for _ in range(m)]
    for x in range(m):
        for y in range(m):
            new_arr[y][m-1-x] = arr[x][y]
    return new_arr

for step in l:
    s = 2**step
    # 부분격자 90도 돌리기
    for i in range(s-1,n,s):
        for j in range(0,n,s):
            new_arr = [[0] * s for _ in range(s)]
            for k in range(s):
                new_arr[k] = array[i-(s-1-k)][j:j+s]

            new_arr = rot90(s,new_arr)
            # print(new_arr)
            for f in range(s):
                array[i-(s-1-f)][j:j + s] = new_arr[f]
            # print(array)
    temp = copy.deepcopy(array)
    # 얼음양 줄이기
    for x in range(n):
        for y in range(n):
            if array[x][y] >0:
                cnt = 0
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if 0 <= nx < n and 0 <= ny < n and array[nx][ny] != 0:
                        cnt += 1
                if cnt < 3:
                    temp[x][y] -= 1
    array = copy.deepcopy(temp)

# 얼음양 확인
visited = [[0]*n for _ in range(n)]
def dfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cnt = 1
    while q:
        sx,sy = q.popleft()
        for d in range(4):
            nx = sx + dx[d]
            ny = sy + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and array[nx][ny] != 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

ice_sum = 0
ice_num = 0
for x in range(n):
    for y in range(n):
        if array[x][y] != 0:
            ice_sum += array[x][y]
            ice_num = max(ice_num, dfs(x,y))

ice_s = sum(array,[])

print(sum(ice_s))
print(ice_num)
