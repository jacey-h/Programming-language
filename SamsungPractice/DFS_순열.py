data = ['a','b','c']
r = 2
visited = [0 for _ in range(len(data))]
answer = []

def dfs(cnt, list):
    if cnt == r:
        answer.append(list[:])
        return
    for i, value in enumerate(data):
        if visited[i] == 1:
            continue
        list.append(value)
        visited[i] = 1
        dfs(cnt+1, list)
        list.pop()
        visited[i] = 0

dfs(0,[])
print(answer)