# 입력
# 설정하기
# 빈칸
# 0~7 은 물고기
# 상어 -1
# 물고기 냄새 -2
from itertools import product
from collections import deque
array = [[[]*5 for _ in range(5)] for _ in range(5)]
m, s = map(int,input().split())

dx8 = [0,-1,-1,-1,0,1,1,1]
dy8 = [-1,-1,0,1,1,1,0,-1]

no_entry = (-1,-2)
fish = (0,1,2,3,4,5,6,7)
for _ in range(m):
    x,y,d = map(int,input().split())
    array[x][y].append(d-1)
sx,sy = map(int,input().split())
array[sx][sy].append(-1)

# print(array)

# 물고기 복제
def fish_copy(array,new_array):
    # copy_array = [[[]*5 for _ in range(5)] for _ in range(5)]
    for x in range(1,5):
        for y in range(1,5):
            for i in array[x][y]:
                if i > -1:
                    new_array[x][y].append(i)
    return new_array

# 물고기 움직임
new_array = [[[] * 5 for _ in range(5)] for _ in range(5)]
def fish_move(array):
    for x in range(1, 5):
        for y in range(1, 5):
            for i in array[x][y]:
                # print(f'i : {i}')
                if i > -1:
                    cnt = 0
                    now = i
                    for d in range(8):
                        cnt += 1
                        nx = x + dx8[now]
                        ny = y + dy8[now]
                        if 0 < nx <= 4 and 0 < ny <= 4 and no_entry not in array[nx][ny]:
                            # print(f'방향전환 {nx,ny, i-d}')
                            new_array[nx][ny].append(i-d)
                            # print(x,y)
                            # print(f'새어레이 : {new_array}')
                            break
                        now = (now-1)%8
                    if cnt == 8:
                        new_array[x][y].append(i)
                elif i == -2:
                    new_array[x][y].append(i)

# 상어가 이동할 수 있는 경로 순열 구하기
dir4 = [1,2,3,4]
dx4 = ["empty",-1,0,1,0]
dy4 = ["empty",0,-1,0,1]

s_move = list(product(dir4, repeat = 3))
# visited = [0 for _ in range(len(dir4))]
#
# def dfs(cnt,list):
#     if cnt == r:
#         s_move.append(list[:])
#         return
#     for i, value in enumerate(dir4):
#         if visited[i] == 1:
#             continue
#         list.append(value)
#         visited[i] = 1
#         dfs(cnt+1, list)
#         list.pop()
#         visited[i] = 0
# dfs(0,[])

# 상어 움직임
def shark_move(s_move,array):
    # print(s_move, array)
    count = 0
    q = deque(s_move)
    # print(q)
    d1 = q.popleft()
    nx = sx + dx4[d1]
    ny = sy + dy4[d1]
    # print(f'nx,ny : {nx,ny}')
    if nx < 1 or nx > 4 or ny < 1 or ny > 4:
        return
    d2 = q.popleft()
    nnx = nx + dx4[d2]
    nny = ny + dy4[d2]
    # print(f'nnx,nny : {nnx,nny}')

    if nnx < 1 or nnx > 4 or nny < 1 or nny > 4:
        return
    d3 = q.popleft()
    nnnx = nnx + dx4[d3]
    nnny = nny + dy4[d3]
    # print(f'nnnx,nnny : {nnnx,nnny}')

    if nnnx < 1 or nnnx > 4 or nnny < 1 or nnny > 4:
        return

    # check1 = 0
    visited = [[0]*5 for _ in range(5)]
    for i in array[nx][ny]:
        # print(f'nx,ny : {array[nx][ny]}')
        if i > -1 and visited[nx][ny] == 0:
            count += 1
            visited[nx][ny] = 1
    #         check1 = 1
    # if check1 == 1:
    #     array[nx][ny] = [-2]
    #
    # check2 = 0
    for i in array[nnx][nny]:
        # print(f'nnx,nny : {array[nnx][nny]}')
        if i > -1 and visited[nnx][nny] == 0:
            count += 1
            visited[nnx][nny] = 1
    #         check2 = 1
    # if check2 == 1:
    #     array[nnx][nny] = [-2]
    #
    # check3 = 0
    for i in array[nnnx][nnny]:
        # print(f'nnnx,nnny : {array[nnnx][nnny]}')
        if i > -1 and visited[nnnx][nnny] == 0:
            count += 1
            visited[nnnx][nnny] = 1
            # check3 = 1
    # if check3 == 1:
    #     array[nnnx][nnny] = [-2]

    return count, nnnx,nnny



# 메인문 실행
smell_list = [[] for _ in range(s)]
for num in range(s):
    # 2. 물고기 이동
    new_array = [[[] * 5 for _ in range(5)] for _ in range(5)]
    fish_move(array)
    # print(new_array)
    # 3. 상어 이동
    s_result = []
    for i in range(len(s_move)):
        if shark_move(s_move[i], new_array) != None:
            cnt, x,y = shark_move(s_move[i], new_array)
            sum_all = s_move[i][0]*100 + s_move[i][1]*10 + s_move[i][2]
            s_result.append([cnt, sum_all, (x,y), i])
    s_result.sort(key=lambda x: (-x[0],x[1]))
    # print(s_result)

    que = deque(s_move[s_result[0][3]])
    # print(que)

    while que:
        d = que.popleft()
        for i in new_array[sx+dx4[d]][sy+dy4[d]]:
            if i > -1:
                new_array[sx+dx4[d]][sy+dy4[d]] = [-2]
            smell_list[num].append((sx+dx4[d],sy+dy4[d]))
        sx += dx4[d]
        sy += dy4[d]

    sx,sy = s_result[0][2][0], s_result[0][2][1]

    # 냄새 지우기
    if num >= 2:
        for i,j in smell_list[num-2]:
            new_array[i][j].remove(-2)

    # 복제 완료
    # print(new_array)
    array = fish_copy(array,new_array)
    array[sx][sy].append(-1)

result = 0
for x in range(1,5):
    for y in range(1,5):
        for i in array[x][y]:
            if i > -1:
                result += 1
# print(array)
print(result)

#### 틀림

# 정답

from itertools import product
f_dir=[(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
s_dir=[(-1,0),(0,-1),(1,0),(0,1)]


M,S=map(int,input().split())
room=[[[]for _ in range(4)] for _ in range(4)]
smell=[[-3]*4 for _ in range(4)]
for _ in range(M):
    x,y,d=map(int,input().split())
    room[x-1][y-1].append(d-1)


def inside(x,y):
    if x<0 or x>=4 or y<0 or y>=4:
        return False
    return True

sx,sy=map(int,input().split())
sx-=1
sy-=1

time=0
for time in range(S):
    # print(time)
    # print(sx,sy)
    # for x in range(4):
    #     print(room[x])
    # print()
    temp=[[[]for _ in range(4)]for _ in range(4)]

    #1 물고기 이동
    #이동한 걸 temp배열에 추가해준다
    for x in range(4):
        for y in range(4):
            if room[x][y]:

                for nd in room[x][y]:
                    flag=False
                    now=nd
                    for d in range(8):
                        nx=x+f_dir[now][0]
                        ny=y+f_dir[now][1]

                        if inside(nx,ny) and  not [nx,ny]==[sx,sy] and smell[nx][ny]+2<time:
                            temp[nx][ny].append(now)
                            flag=True
                            break
                        now=(now-1)%8
                    #아무데도 못간다-->그 자리에 넣어준다
                    if not flag:
                        temp[x][y].append(nd)
    # for x in range(4):
    #     print(temp[x])
    # print()
    #2. 상어이동
    #중복조합으로 케이스를 미리 구한거에다가 넣어보자
    #max를 -1로 초기화한 이유-->어떤 케이스로 움직이든 하나도 못먹는 케이스 존재
    #만약 0으로 초기화를 해놓으면, 만약 아무것도 못먹으면 상어가 움직이지 않는다
    #그러니, 0이 될 때에 가장 사전순인 상상상이라도 받도록 해준다
    eat_max=-1
    go=[]
    for case in list(product([0, 1, 2, 3], repeat=3)):

        tx=sx
        ty=sy
        t_fish=0
        flag=False
        move=set()
        for num in case:

            tx+=s_dir[num][0]
            ty+=s_dir[num][1]

            #범위벗어나면 넘김
            if not inside(tx,ty):
                flag=True
                break
            if not (tx,ty) in move:
                t_fish+=len(temp[tx][ty])
                move.add((tx,ty))

        if flag:
            continue

        if eat_max<t_fish:
            eat_max=t_fish
            go=list(case)



    #3. 이동하면서 물고기 먹어준다
    for num in go:
        sx+=s_dir[num][0]
        sy+=s_dir[num][1]
        if temp[sx][sy]:
            smell[sx][sy]=time
        temp[sx][sy].clear()


    #이전에 복제한 거에 더해준다
    for x in range(4):
        for y in range(4):
            room[x][y]+=temp[x][y]

    # print()
    # for x in range(4):
    #     print(room[x])
    # print()

answer=0
for x in range(4):
    for y in range(4):
        if room[x][y]:
            answer+=len(room[x][y])

print(answer)