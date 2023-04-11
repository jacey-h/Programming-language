n, m = map(int,input().split())
array = []
move_list = []

for _ in range(n):
    array.append(list(map(int,input().split())))

for _ in range(m):
    x, y = map(int,input().split())
    move_list.append((x,y))


dx8 = ['empty',0,-1,-1,-1,0,1,1,1]
dy8 = ['empty',-1,-1,0,1,1,1,0,-1]
clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]

dx4 = [-1,-1,1,1]
dy4 = [-1,1,1,-1]

for d,s in move_list:
    cloud_list = []
    for cloud in clouds:       
        nx = (cloud[0] + (dx8[d]*s)) % n
        ny = (cloud[1] + (dy8[d]*s)) % n
        array[nx][ny] += 1
        cloud_list.append((nx,ny))

    for x,y in cloud_list:
        for k in range(4):
            nx = x+dx4[k]
            ny = y+dy4[k]
            if 0 <= nx< n and 0 <= ny < n:
                if array[nx][ny] > 0:
                    array[x][y] += 1
        
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if array[x][y] >=2 and ((x,y) not in cloud_list):
                array[x][y] -= 2
                new_clouds.append((x,y))  
    clouds = new_clouds  

result = 0
for i in range(n):
 result += sum(array[i])

print(result)

##### 수정전 
# 둘다 python3 로 시간초과남 / pypy3 해야 정답처리됨 
n, m = map(int,input().split())
array = []
d = []
s = []

for _ in range(n):
    array.append(list(map(int,input().split())))

for _ in range(m):
    x, y = map(int,input().split())
    d.append(x)
    s.append(y)


dx8 = ['empty',0,-1,-1,-1,0,1,1,1]
dy8 = ['empty',-1,-1,0,1,1,1,0,-1]
clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
cloud_list = []

dx4 = [-1,-1,1,1]
dy4 = [-1,1,1,-1]

for i in range(m):
    for cloud in clouds:
       
        nx = (cloud[0] + (dx8[d[i]]*s[i])) % n
        ny = (cloud[1] + (dy8[d[i]]*s[i])) % n
        array[nx][ny] += 1
        cloud_list.append((nx,ny))
    clouds = []
    for j in range(len(cloud_list)):
        for k in range(4):
            nx = cloud_list[j][0]+dx4[k]
            ny = cloud_list[j][1]+dy4[k]
            if 0 <= nx< n and 0 <= ny < n:
                if array[nx][ny] != 0:
                    array[cloud_list[j][0]][cloud_list[j][1]] += 1

    for x in range(n):
        for y in range(n):
            if array[x][y] >=2 and ((x,y) not in cloud_list):
                array[x][y] -= 2
                clouds.append((x,y))
    cloud_list = []
    
result = 0
for i in range(n):
 result += sum(array[i])

print(result)