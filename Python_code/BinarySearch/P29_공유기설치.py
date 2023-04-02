from itertools import combinations
n, c  = map(int,input().split())
array =  []

for i in range(n):
  array.append(int(input()))
array.sort()
data = list(combinations(array,c))
count = []
max_d = 0
for k in data:
  for i in range(c-1):
    for j in range(i+1,c):
      count.append(k[j]-k[i])
  max_d = max(max_d, min(count))
  count = []
print(max_d)

#### 답

n, c  = map(int,input().split())
array =  []

for i in range(n):
  array.append(int(input()))
array.sort()

start = array[1] - array[0]
end = array[-1] - array[0]
result = 0

while start <= end:
  mid = (start+end)//2
  value = array[0]
  count = 1
  for i in range(1,n):
    if array[i] >= value + mid:
      value = array[i]
      count += 1
  if count >= c:
    start = mid +1
    result = mid
  else:
    end = mid -1

print(result)
    