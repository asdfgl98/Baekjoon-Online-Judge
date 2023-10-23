def solution(s, n):
    answer = ''
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    a = 'abcdefghijklmnopqrstuvwxyz'
    s = list(s)
    for i in s:
        if i != ' ':
            if i.isupper():
                idx = A.index(i)+n
                if idx >= len(A):
                    idx -= (len(A))
                answer += A[idx]
            else:
                idx = a.index(i)+n
                if idx >= len(a):
                    idx -= (len(a))
                answer += a[idx]
        else:
            answer += ' '
    
        
    
    return answer