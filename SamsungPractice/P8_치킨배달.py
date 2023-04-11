n, m = map(int,input().split())

array = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    array[i][1:] = list(map(int,input().split()))

# 치킨 집 조합구하기
data = []
for x in range(1,n+1):
    for y in range(1,n+1):
        if array[x][y] == 2:
            data.append((x,y))
comb = []
def dfs(idx,list):
    if len(list) == m:
        comb.append(list[:])
        return
    for i in range(idx,len(data)):
        dfs(i+1, list+[data[i]])
dfs(0,[])

# 치킨 거리 구하기
def distance(x,y):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if array[i][j] == 1:
                x_dis = i - x
                y_dis = j - y
                if x_dis < 0:
                    x_dis *= -1
                if y_dis < 0:
                    y_dis *= -1
                dis_array[i][j] = min(dis_array[i][j],x_dis+y_dis)

# 도시 치킨거리 최솟값 구하기
def city_distance():
    cnt = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if array[i][j] == 1:
                cnt += dis_array[i][j]
    return cnt

#### 메인문
result = []
for loc in comb:
    dis_array = [[2 * n] * (n + 1) for _ in range(n + 1)]
    for x,y in loc:
        distance(x,y)
    result.append(city_distance())

print(min(result))

