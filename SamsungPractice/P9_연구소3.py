from collections import deque
# 입력받기
n, m = map(int,input().split())
graph = []
zero_check = 0
for _ in range(n):
    temp = list(map(int,input().split()))
    graph.append(temp)

    if 0 not in temp:
        zero_check += 1

# 바이러스 좌표 세기
virus = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            virus.append((x,y))
            graph[x][y] = -1

# 바이러스 개수 중 M개의 조합구하기
comb = []

def dfs(idx, list):
    if len(list) == m:
        comb.append(list[:])
        return
    for i in range(idx, len(virus)):
        dfs(i+1, list+[virus[i]])
dfs(0,[])
# 바이러스 확산
dx = [-1,0,1,0]
dy = [0,1,0,-1]

min_time = []
def bfs(graph,comb):
    array = [[0]*n for _ in range(n) ]
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            array[i][j] = graph[i][j]
            if graph[i][j] == 1:
                visited[i][j] = True

    q = deque(comb)
    time = 0
    while q:
        x, y = q.popleft()
        visited[x][y] = True
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and array[nx][ny] != 1 and not visited[nx][ny]:
                if array[nx][ny] == -1:
                    for dc in range(4):
                        nnx = nx + dx[dc]
                        nny = ny + dy[dc]
                        if 0 <= nnx < n and 0 <= nny < n and not visited[nnx][nny]:
                            array[nx][ny] = array[x][y] + 1
                            q.append((nx, ny))
                            visited[nx][ny] = True
                        else:
                            array[nx][ny] = array[x][y]
                            visited[nx][ny] = True

                else:
                    array[nx][ny] = array[x][y]+1
                    q.append((nx,ny))
                    time = max(time,array[nx][ny])
                    visited[nx][ny] = True
    # print(f'comb : {comb}')
    # print(f'array : {array}')
    # print(f'visited : {visited}')
    for check in visited:
        if False in check:
            time = 11
    min_time.append(time+1)
    # print(time + 1)

if zero_check == n:
    print(0)
else:
    for i in comb:
        bfs(graph,i)
    min_time.sort()
    if min_time[0] > 10:
        print(-1)
    else:
        print(min_time[0])

# 틀림

####### 정답 코드

from collections import deque
from itertools import combinations
import sys


input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)


def bfs(active):
    q = deque()
    visited = [[-1] * n for _ in range(n)]
    result = 0

    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny])
                elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    if list(sum(visited, [])).count(-1) != wall_cnt:
        return inf
    return result


wall_cnt = 0
virus = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            wall_cnt += 1
        elif graph[i][j] == 2:
            virus.append((i, j))

ans = inf
for active in combinations(virus, m):
    ans = min(ans, bfs(active))

print(ans if ans != inf else -1)