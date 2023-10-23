def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(1,len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    answer = sorted(list(set(answer)))
    return answer