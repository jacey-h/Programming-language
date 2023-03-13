n = int(input())
array = []
for i in range(n):
  array.append(tuple(input().split()))

array = sorted(array, key= lambda x: x[1],reverse=False)

for i in array:
  print(i[0], end=" ")