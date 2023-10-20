def solution(s):
    answer = ''
    n = sorted(s)
    n.reverse()
    answer = ''.join(n)
    return answer