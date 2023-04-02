########## 데이터 입력 구간 ##############
# 입력받기 input 대신 사용
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수
n, m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visited = [False]*(n+1)
distance = [INF]*(n+1)

for i in range(n+1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

######### 방문하지 않은 노드 중 최단거리가 가장 작은거 / 즉, 다음순서로 방문 할 노드 ##########
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
    
########### 다익스트라 ##########
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for _ in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

############## 값 계산하고 출력하기 ##################
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
