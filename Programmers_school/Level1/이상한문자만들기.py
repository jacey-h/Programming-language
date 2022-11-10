def solution(s):
    answer = []
    cnt = 0
    for i in list(s):
        if i == ' ':
            cnt = 0
            answer.append(' ')
        elif cnt % 2 == 0:
            answer.append(i.upper())
            cnt += 1
        else:
            answer.append(i.lower())
            cnt += 1

    return ''.join(answer)