# 내가 푼거 어렵게 생각함
n = int(input())

d = [0]*1000

d[0] = 1
d[1] = 3

if n%2 == 0:
  d[n-1] = 2*d[n-2]
  for i in range((n-3)//2+1):
    d[n-1] += 2*(d[i]*d[n-(3+i)])
  d[n-1] -= (n-2)
else:
  d[n-1] = d[n-n//2]*d[n-n//2]
  for i in range(2,n//2+2):
    d[n-1] += 2*d[n-i]
  d[n-1] -= (n-2)

print(d[n-1])

# 답
n = int(input())

d = [0]*1001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
  d[i] = (d[i-1]+d[i-2]*2) % 796796
print(d[n])