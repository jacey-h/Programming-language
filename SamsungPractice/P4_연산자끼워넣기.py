from itertools import permutations
from collections import deque
n = int(input())
num = list(map(int,input().split()))
data_num = list(map(int,input().split()))

data = []
for i in range(4):
    for j in range(data_num[i]):
        if i == 0:
            data.append('+')
        if i == 1:
            data.append('-')
        if i == 2:
            data.append('*')
        if i == 3:
            data.append('/')

array = set(list(permutations(data,n-1)))
data = list(array)
count = []
for i in range(len(data)):
    temp = deque(num)
    for j in range(n-1):
        a = temp.popleft()
        b = temp.popleft()
        if data[i][j] == '+':
            temp.appendleft(a+b)
        if data[i][j] == '-':
            temp.appendleft(a-b)
        if data[i][j] == '*':
            temp.appendleft(a*b)
        if data[i][j] == '/':
            if a < 0 and b > 0:
                temp.appendleft(-(-a//b))
            else:
                temp.appendleft(a//b)
    count.append(temp.pop())
print(max(count))
print(min(count))
