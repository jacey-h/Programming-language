n = int(input())
array = list(map(int,input().split()))
b, c = map(int,input().split())

count = 0
for i in range(n):
  array[i] -=  b
  count += 1
for j in range(n):
  if array[j] > 0:
    if array[j]%c == 0:
      count += (array[j]//c)
    else:
      count = count +1 +(array[j]//c)

print(count)