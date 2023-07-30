def solution(n):
    answer = 0
    
    i=n-1
    while(i!=1):
        if n%i==1 :
            answer = i
            
        i-=1
            
    
    return answer