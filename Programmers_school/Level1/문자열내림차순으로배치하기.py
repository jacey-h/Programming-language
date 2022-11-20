# def solution(s):
#     answer = list(map(ord, list(s)))
#     answer.sort(reverse = True)
    
#     return ''.join(list(map(chr,answer)))

def solution(s):

	return ''.join(sorted(s, reverse=True))