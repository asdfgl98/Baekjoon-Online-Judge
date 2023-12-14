def solution(s):
    answer = True
        
    # if s[0] == ')' or s[-1] == '(':
    #     answer = False
    # elif len(s) % 2 != 0:
    #     answer = False
    # elif s.count(')') != s.count('('):
    #     answer = False
    cnt = 0    
    for i in s:
        if cnt < 0 :
            answer = False
            
        if i == '(':
            cnt += 1
        elif i == ')':
            cnt += -1
    
    if cnt != 0:
        answer = False
        
        
        

    return answer