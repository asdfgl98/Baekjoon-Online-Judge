def solution(food):
    answer = []
    for i in range(len(food)):
        if food[i]//2 != 0:
            for j in range((food[i]//2)):
                answer.append(str(i))
    answer.append('0')
    
    for i in range(len(answer)-2, -1, -1):
        answer.append(str(answer[i]))
        
    return ''.join(answer)