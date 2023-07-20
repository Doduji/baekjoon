def solution(n):
    answer = 0
    num = str(n)
    
    for i in range(0, len(num)) :
        answer += int(num[i])
    
    return answer