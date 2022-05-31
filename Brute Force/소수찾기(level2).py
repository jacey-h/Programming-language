from itertools import permutations
def solution(numbers):
    def prime(n):
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    numlist=[]
    for i in numbers:
        numlist.append(int(i))
    total = [0]*len(numlist)
    for i in range(1,len(numlist)+1):
        total[i-1]=list(permutations(numlist,i))
    too=[]
    count=0
    for i in range(len(total)):
        for j in range(len(total[i])):
            too.append(list(map(str,(total[i][j]))))
    llist=[]
    for i in range(len(too)):
        a=''.join(too[i])
        llist.append(a)
    llist = set(llist)

    for i in llist:
        if (i[0]!='0') and (i!='1'):
            if prime(int(i)):
                count+=1
    result = count
    return result