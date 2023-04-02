import heapq
n, m, c = map(int,input().split())
INF = int(1e9)
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
  x, y, z = map(int,input().split())
  graph[x].append((y,z))

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
        heapq.heappush(q,(cost,i[0]))
dijkstra(c)
print(distance)
total_time = 0
total_city = 0
for i in range(1,n+1):
  if distance[i] != INF:
    total_time = max(total_time,distance[i])
    if i != c:
      total_city += 1

print(total_city, total_time)
      