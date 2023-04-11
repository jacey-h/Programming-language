visited = [[-1]*3 for _ in range(3)]
visited[0][1] = 5

a = list(sum(visited,[])).count(-1)
print(a)
print(visited)
print(sum(visited,[]))