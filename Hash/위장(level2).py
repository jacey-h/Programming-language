from collections import Counter
def solution(clothes):
    cnt=[]
    for i in range(len(clothes)):
        cnt.append(clothes[i][1])
    count = Counter(cnt)
    clist = list(count.values())

    if len(clist)==1: 
        return clist.pop()
    else:
        csum = [x+1 for x in clist]
        mul=1
        for i in csum:
            mul*=i
    return mul-1