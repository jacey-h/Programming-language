# 내 풀이 - 조합 라이브러리 활용
# m이 무게 수가 아닌 최대 무게이므로 답이 틀림!
from itertools import combinations
n, m = map(int,input().split())
array = list(map(int,input().split()))

num = len(list(combinations(array,2)))
print(num-(n-m))

# 정답 풀이
n, m = map(int,input().split())
array = list(map(int,input().split()))

data = [0]*11
for i in array:
  data[i] += 1

result = 0
for i in range(1,len(m)+1):
  n -= data[i]
  result += data[i]*n
print(result)