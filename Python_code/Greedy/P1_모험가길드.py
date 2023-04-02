n = int(input())
array = list(map(int,input().split()))
array.sort()

#x = 0
num = 0
group = 0

for i in array:
#  x += i
  num += 1
  if num >= i: # 같은게 아니라 크거나 같아야함
    group += 1
    num = 0
#  x = 0
# x 사용하지 않아도 됨 

print(group)    
  