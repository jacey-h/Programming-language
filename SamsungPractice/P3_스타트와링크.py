from itertools import combinations

n = int(input())
array=[]
num = []
for i in range(n):
  num.append(i+1)
  array.append(list(map(int,input().split())))

data = list(combinations(num,n//2))
count  = [0]*(len(data)//2)
for i in range(len(data)//2):
  for x in range((n//2)-1):
    for y in range(x+1,n//2):
       count[i] += (array[data[i][x]-1][data[i][y]-1] + array[data[i][y]-1][data[i][x]-1]) - (array[data[-i-1][x]-1][data[-i-1][y]-1] + array[data[-i-1][y]-1][data[-i-1][x]-1])
for k in range(len(count)):
  if count[k] <0:
    count[k] *= -1
print(min(count))