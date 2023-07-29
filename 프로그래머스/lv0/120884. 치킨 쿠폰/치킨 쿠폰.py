def solution(chicken):
    answer = 0
    
    while(chicken>9) :
        answer+= int(chicken/10)
        chicken = int(chicken/10) + int(chicken%10)
    
    
    return answer