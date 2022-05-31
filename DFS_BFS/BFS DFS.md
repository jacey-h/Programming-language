# BFS / DFS

## 깊이우선탐색 (DFS)

![ass.JPG](BFS%20DFS%20c74026cde464473eb92e18814a08bbcf/ass.jpg)

```python
adj_list = [
	[],  # 0은 없음
	[2,3,8],  # 1번 노드는 2,3,8번 노드랑 인접해있음
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False]*9

dfs(adj_list,1,visited)
```

```python
def dfs(adj_list,v,visited):
	visited[v] = True
	print(v, end=' ')
	
	for i in adj_list[v]:
		if not visited[i]:
			dfs(adj_list, i, visited)
```

- 데크 사용법

```python
from collections import deque

deq = deque()

# 데크의 왼쪽 끝에 삽입 (시작)
deq.appendleft(10)

# 데크의 오른쪽 끝에 삽입 (끝)
deq.append(0)

# 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
deq.popleft()

# 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제
deq.pop()
```

## 너비우선탐색 (BFS)

![fd.JPG](BFS%20DFS%20c74026cde464473eb92e18814a08bbcf/fd.jpg)

```python
adj_list = [
	[],  # 0은 없음
	[2,3,8],  # 1번 노드는 2,3,8번 노드랑 인접해있음
	[1,7],
	[1,4,5],
	[3,5],
	[3,4],
	[7],
	[2,6,8],
	[1,7]
]
visited = [False]*9

bfs(adj_list,1,visited)
```

```python
from collections import deque

def bfs(adj_list,start,visited):
	queue = deque([start])
	visited[start] = True
	
	while queue:
		v = queue.popleft()
		print(v, end=' ')
		
		for i in adj_list[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
```

## 음료수 얼려 먹기

![KakaoTalk_20220521_192526294.png](BFS%20DFS%20c74026cde464473eb92e18814a08bbcf/KakaoTalk_20220521_192526294.png)

```python
def dfs(x,y):
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  if graph[x][y] == 0:
    graph[x][y]=1
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  return False

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

result = 0
for i in range(n):
  for j in range**(m):
    if dfs(i,j) ==True:
      result += 1**
print(result)
```

## 프로그래머스 타겟넘버

내아이디어 : 데크를 사용해서 1,2번째 꺼내서 계산후 다시 데크에 넣음 → 반복

근데 +, - 가 문제 (2번째에도 못품)

```python
from collections import deque
def solution(numbers, target):
    answer = 0
    queue = deque()
    n = len(numbers)
    queue.append([numbers[0],0])
    queue.append([-1*numbers[0],0])
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer
```

모든거에 +,- 계속해주면됨

![KakaoTalk_20220525_175633407.jpg](BFS%20DFS%20c74026cde464473eb92e18814a08bbcf/KakaoTalk_20220525_175633407.jpg)

![KakaoTalk_20220525_175633872.jpg](BFS%20DFS%20c74026cde464473eb92e18814a08bbcf/KakaoTalk_20220525_175633872.jpg)