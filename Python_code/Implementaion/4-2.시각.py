n = int(input())
count = 0
h,m,s=0,0,0
while True:
  s+=1
  if s==60:
    m+=1
    s=0
  if m==60:
    h+=1
    m=0
  present_time = ''.join(map(str,[h,m,s]))
  if '3' in present_time:
    count+=1
  if h==n and m==59 and s==59:
    break 
print(count)

# 정답
h = int(input())

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)