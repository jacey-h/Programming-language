# 이차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행
    m = len(a[0]) # 열
    result = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def check(new_lock):
    lock_length = len(new_lock) //3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(n*2):
            for y in range(n*2):
                for i in range(m): # 열쇠 넣기
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                for i in range(m): # 열쇠 뺴기
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

# def solution(key, lock):
#     n = len(lock)
#     m = len(key)
#     array = [[0]*3*n for _ in range(3*n)]
#     answer = False
#     for i in range(n):
#         array[n+i][n:2*(n)] = lock[i] # 한줄씩 넣으려고 함 / 하나씩 넣기로 바꾸기
#     new_key = [[0]*m for _ in range(m)]
#     for i in range(4):
#         if i != 0:
#             key = new_key
#             print(f'key : {key}')

#             for x in range(m):  # 여기 틀림 
#                 for y in range(m):            
#                     new_key[y][m-x-1] = key[x][y]
#         else:
#             new_key  = key
#         print(f'new_key : {new_key}')
#         for k in range(3*n-m):
#             for j in range(m):
#                 array[k+j][k:m+k] = new_key[j]  

#             count = 0
#             for h in range(n):
#                 if sum(array[n+h][n:2*(n)]) == n:
#                     count += 1
#             if count == n:
#                 answer = True

#     return True

###################### 답