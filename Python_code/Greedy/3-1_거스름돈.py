n=int(input())

count=0
while True:
  if n>=500:
    count+=n//500
    n%=500
  elif n>=100:
    count+=n//100
    n%=100
  elif n>=50:
    count+=n//50
    n%=50
  elif n>=10:
    count+=n//10
    break    
print(count)

# 정답

n=1260
count=0

coin_types=[500,100,50,10]

for coin in coin_types:
    count += n//coin
    n%=coin

print(count)