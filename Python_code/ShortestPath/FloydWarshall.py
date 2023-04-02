INF = int(1e9)
n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

####### 자기 자신으로 가는 비용은 0 #####
for a in range(1,n+1):
    for b in range(i,n+1):
        if a == b:
            graph[a][b] =0

####### 입력 받기 #######
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c

######## 플로이드 워셜 #####
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

######## 출력 ########
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b], end=" ")
    print()