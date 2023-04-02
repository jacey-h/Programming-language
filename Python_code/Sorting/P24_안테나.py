n = int(input())
array = list(map(int,input().split()))
array.sort()

count = 0
result = []
for i in array:
  for j in array:
    if i >= j:
      count += (i-j)
    else:
      count += (j-i)
  result.append((i,count))
  count = 0

result.sort(key = lambda loc : loc[1])
print(result[0][0])

# 정답 - 중간값이 가장 작음

n = int(input())
array = list(map(int,input().split()))
array.sort()
print(array[(n-1)//2])