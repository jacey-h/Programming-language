data = [1,2,3]
r = 2
answer = []
list = []
def dfs(cnt):
    if cnt == r:
        answer.append(list[:])
        return
    for i in data:
        list.append(i)
        dfs(cnt+1)
        list.pop()

dfs(0)
print(answer)