def solution(n):
    answer = -1
    i=1
    
    while(n>=(i*i)) :
        if (i*i)==n :
            answer=(i+1)*(i+1)
        i+=1
    
    
    return answer