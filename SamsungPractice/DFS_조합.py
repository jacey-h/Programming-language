data = [1,2,3,4]
r = 2
answer = []

def dfs(idx,list):
    if len(list) == r:
        answer.append(list[:])
        return
    for i in range(idx,len(data)):
        dfs(i+1, list+[data[i]])

dfs(0,[])
print(answer)