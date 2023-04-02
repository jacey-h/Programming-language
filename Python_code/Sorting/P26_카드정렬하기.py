n = int(input())
array = []
for i in range(n):
  array.append(int(input()))

array.sort(reverse=True)
count = 0
while len(array) > 1:
  a = array.pop()
  b = array.pop()
  count += (a+b)
  array.append(a+b)
  array.sort(reverse=True)

print(count)