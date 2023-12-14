def solution(s):
    answer = ''
    s = s.lower().split(" ")
    result = []
    for i in s:
        if i != "":
            result.append(i.capitalize())
        else:
            result.append("")
                
    answer = " ".join(result)
    
    # for i in s:
    #     for idx,j in enumerate(i):
    #         if idx == 0:
    #             answer += j.upper()
    #         else:
    #             answer += j.lower()
    #     answ

    return answer