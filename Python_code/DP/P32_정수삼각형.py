n = int(input())
array = []
for _ in range(n):
  array.append(list(map(int,input().split())))
for i in range(1,n):  # 행
  for j in range(n):  # 열
    if j > i:
      break
    if j-1 < 0: # j==0:
      left = 0
    else:
      left = array[i-1][j-1]
    if j > i-1:  # j == i:
      right = 0
    else:
      right = array[i-1][j]
    array[i][j] = array[i][j] + max(left,right)

print(max(array[n-1]))