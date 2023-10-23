def solution(n, arr1, arr2):
    answer = []

    result = []
        
    for i in range(n):
        result.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('0', ' ').replace('1', '#'))
                      
    for i in result:
        answer.append(i)        
    
    return answer