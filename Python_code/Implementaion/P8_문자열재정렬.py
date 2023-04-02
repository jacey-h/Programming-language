s = input()
sum = 0
data = []

for i in s:
  if ord(i) < 65: # i.isalpha()
    sum += int(i)
  else:
    data.append(i)
data.sort()

for i in data:
  print(i, end="")
if sum != 0:
  print(str(sum))

# 더 쉬운 방법
if sum != 0:
  data.append(str(sum))
print(''.join(data))
