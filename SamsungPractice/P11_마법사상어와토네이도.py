n = int(input())
array = [list(map(int,input().split())) for _ in range(n)]

dx = [0,1,0,-1]
dy = [-1,0,1,0]
rate = [2,2,10,10,7,7,1,1,5]

west = [(-2,0),(2,0),(-1,-1),(1,-1),(-1,0),(1,0),(-1,1),(1,1),(0,-2)]
south = [(0,-2),(0,2),(1,-1),(1,1),(0,-1),(0,1),(-1,-1),(-1,1),(2,0)]
east = [(-2,0),(2,0),(-1,1),(1,1),(-1,0),(1,0),(-1,-1),(1,-1),(0,2)]
north = [(0,2),(0,-2),(-1,1),(-1,-1),(0,1),(0,-1),(1,1),(1,-1),(-2,0)]
sand_dir = [west,south,east,north]

def init_grid():
    x = y = int(n/2)
    direction = move_count  = 0
    dist = 1
    result = 0
    while True:
        move_count += 1
        for i in range(dist):
            nx = x + dx[direction]
            ny = y + dy[direction]

            if (nx,ny) == (0,-1):
                return result
            # 모래
            if array[nx][ny] != 0: # 모래가 있다면
                # print((nx, ny))
                a = 0
                for j in range(9):
                    sx = nx + sand_dir[direction][j][0]
                    sy = ny + sand_dir[direction][j][1]

                    sand_rate = int(array[nx][ny] * (rate[j] / 100))
                    if 0 <= sx < n and 0 <= sy < n:
                        array[sx][sy] += sand_rate
                        a += sand_rate
                        # print(f'9개중 : {sand_rate}')
                        # print(f'a: {a}')
                    else:
                        result += sand_rate
                        a += sand_rate
                sx = nx + dx[direction]
                sy = ny + dy[direction]
                sand_rate = (array[nx][ny] - a)
                if 0 <= sx < n and 0 <= sy < n:
                    array[sx][sy] += sand_rate
                else:
                    # print('this')
                    result += sand_rate
                # print(f'1개중 : {sand_rate}')
                # print(f'a: {a}')

                array[nx][ny] = 0
                # print(array)
                # print(result)
                # print(f'dir : {direction}')


            x,y = nx,ny

        if move_count == 2:
            dist += 1
            move_count = 0
        direction = (direction + 1) % 4

print(init_grid())