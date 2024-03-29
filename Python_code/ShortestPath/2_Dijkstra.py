# 힙 사용
import heapq

########## 데이터 입력 구간 ##############
# 입력받기 input 대신 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for i in range(n+1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

########### 다익스트라 ##########
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
############## 값 계산하고 출력하기 ##################
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
