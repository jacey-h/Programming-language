def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        i = commands[index][0]
        j = commands[index][1]
        k = commands[index][2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])

    return answer