def solution(n):
    answer = 1
    
    for i in range(1, n) :
        num = 0
        for j in range(i, n) :
            num+=j
            if num == n :
                answer+=1
                break
            if num>n :
                break
    
    return answer