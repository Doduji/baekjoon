def solution(n, k):
    answer = 0
    
    service = int(n/10)

    
    answer = (n*12000)+((k-service)*2000)
    
    return answer