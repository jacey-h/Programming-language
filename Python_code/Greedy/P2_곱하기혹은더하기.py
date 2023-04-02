n = input()
result = 1
for i in range(len(n)):
  if '0' != n[i]:
    result *= int(n[i])
print(result)

# 답
# 1일 경우 곱하는 것보다 더하는게 더 커짐 
n = input()
result = int(n[0])
for i in range(1,len(n)):
  if int(n[i]) <= 1 or result <= 1:
    result += int(n[i])
  else:
    result *= int(n[i])
print(result)