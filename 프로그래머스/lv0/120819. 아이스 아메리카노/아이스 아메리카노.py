def solution(money):
    answer = []
    count = 0
    
    while(money>=5500) :
        count+=1
        money-=5500
            
            
    answer.append(count)
    answer.append(money)
    
    return answer