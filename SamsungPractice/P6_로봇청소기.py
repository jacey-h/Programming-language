# from collections import deque
#
# n,m = map(int,input().split())
# r,c,d = map(int,input().split())
#
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))
# # 북동남서
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# dir = [0,1,2,3]
#
# def bfs(x,y,d):
#     result = 0
#     q = deque()
#     q.append((x,y))
#
#     while q:
#         sx,sy = q.popleft()
#         if graph[sx][sy] == 0:
#             graph[sx][sy] = 2
#             result += 1
#         cnt = 0
#
#         for dc in range(4):
#             nx = sx + dx[dc]
#             ny = sy + dy[dc]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if graph[nx][ny] == 0:
#                     cnt += 1
#         if cnt == 0:
#             bx = sx + dx[d-2]
#             by = sy + dy[d-2]
#             if 0 <= bx < n and 0 <= by < m:
#                 if graph[bx][by] == 1:
#                     return result
#                 else:
#                     q.append((bx,by))
#
#         else:
#             d = dir[d-1]
#             fx = sx + dx[d]
#             fy = sy + dy[d]
#
#             if 0 <= fx < n and 0 <= fy < m:
#                 if graph[fx][fy] == 0:
#                     q.append((fx,fy))
#                 else:
#                     q.append((sx,sy))
#             else:
#                 q.append((sx,sy))
#
# answer = bfs(r,c,d)
# print(answer)


# 수정 후
from collections import deque

n,m = map(int,input().split())
r,c,d = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
# 북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dir = [0,1,2,3]

def bfs(x,y,d):
    result = 0
    q = deque()
    q.append((x,y))

    while q:
        sx,sy = q.popleft()
        if graph[sx][sy] == 0:
            graph[sx][sy] = 2
            result += 1
        cnt = 0

        for i in range(4):
            nx = sx + dx[(d-1)%4]
            ny = sy + dy[(d-1)%4]
            d = (d-1)%4

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                q.append((nx,ny))
                break

            elif i == 3:
                bx = sx + dx[d-2]
                by = sy + dy[d-2]
                if 0 <= bx < n and 0 <= by < m:
                    if graph[bx][by] == 1:
                        return result
                    else:
                        q.append((bx,by))


answer = bfs(r,c,d)
print(answer)
