from collections import deque

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)

# result = [[0] for _ in range(n+1)]

def find_city(graph,x,n):
  result = [0]*(n+1)  # 답지 :처음을 -1 로 둠
  queue = deque([x])
  while queue:
    start = queue.popleft()
    for i in graph[start]:
      queue.append(i)
      if result[i] == 0:
        result[i]  = result[start] + 1
  return result

count = 0
result = find_city(graph,x,n)

if k not in result:
  print(-1)
else:
  for i in range(n+1):
    if result[i] == k:
      print(i)

# 답지
# check = False
# for i in range(n+1):
#   if result[i] == k:
#     print(i)
#     check = True
# if check == False:
#   print(-1)
      
      
    
  