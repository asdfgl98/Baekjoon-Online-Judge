def solution(n, words):
    answer = []
    round = 0
    cnt = 0
    while True:
        round += 1
        for i in range(n):
            try:
                if len(answer) == 0:
                    answer.append(words[i])
                    print(answer)
                else:
                    if words[i] not in answer and answer[-1][-1] == words[i][0]:
                        answer.append(words[i])
                        print(answer)
                    else:
                        return [i+1, round]
            except:
                if len(words) == 0:
                    return [0,0]
        else:
            words = words[n:]
                    
        
                

    return answer