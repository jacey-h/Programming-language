def solution(brown, yellow):
    yx=[]
    yy=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            if i>=yellow//i:
                yx.append(i)
                yy.append(yellow//i)
    bx = [x+2 for x in yx]
    by = [x+2 for x in yy]

    for i in range(len(yx)):
        if yx[i]*yy[i] == yellow and (bx[i]*by[i]-yx[i]*yy[i])==brown:
            return [bx[i],by[i]]