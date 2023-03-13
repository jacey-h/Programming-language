array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

alist = [0]*(max(array)+1)

for i in array:
  alist[i] +=1

for i in range(len(alist)):
  for j in range(alist[i]):
    print(i, end=" ")