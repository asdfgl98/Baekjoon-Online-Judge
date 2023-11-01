def solution(lottos, win_nums):
    answer = []
    lottos.sort()
    lottos.reverse()
    for i in range(len(lottos)):
        if lottos[i] == 0:
            del win_nums[0]            
        elif lottos[i] in win_nums:
            del win_nums[win_nums.index(lottos[i])]
    if len(win_nums) == 6:
        answer.append(6)
    else:
        answer.append(len(win_nums)+1)
        
    if lottos.count(0) == 6:
        answer.append(6)
    elif len(win_nums) >= 5:
        answer.append(6)
    else:
        answer.append(len(win_nums)+lottos.count(0)+1)
        
    return answer