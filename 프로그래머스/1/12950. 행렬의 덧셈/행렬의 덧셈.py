def solution(arr1, arr2):
    answer = [[]]
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr1[i][j] += arr2[i][j]
        
    answer = arr1
    
    return answer