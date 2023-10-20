def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    answer.append(arr[0])
    n = 0
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
            
       
            
            
        
    return answer