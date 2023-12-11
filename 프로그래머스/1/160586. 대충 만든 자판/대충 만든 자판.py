def solution(keymap, targets):
    answer = []  
    
    for i in targets:
        if all(char in ''.join(keymap) for char in i):
            cnt = 0
            for j in i:
                try:
                    result = min((s.index(j), s) for s in keymap if j in s)
                    print(j,result)
                    cnt += result[0]+1
                except ValueError:
                    answer.append(-1)
                    break   
            if cnt != 0:
                answer.append(cnt)
        else:
            answer.append(-1)

    
    return answer