def solution(cards1, cards2, goal):
    answer = ''
    result = 0
    for i in goal:
        if len(cards1) > 0:
            try:
                if i == cards1[0]:
                    del cards1[0]
                    result += 1
                    continue
                elif i == cards2[0]:
                    del cards2[0]
                    result += 1
                    continue
            except:
                pass
        elif len(cards2) > 0:
            if i == cards2[0]:
                del cards2[0]
                result += 1
                continue
        else:
            break
    if len(goal) == result:
        return 'Yes'
    else:
        print(result)
        return 'No'
                


    return answer