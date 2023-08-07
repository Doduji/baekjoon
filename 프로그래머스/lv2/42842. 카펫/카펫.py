def solution(brown, yellow):
    answer = []
    
    y = 1
    while(True) :
        if yellow%y==0 : 
            x=int(yellow/y)
            if (x+2)*(y+2)==(brown+yellow) :
                answer.append(x+2)
                answer.append(y+2)
                break
        y+=1
    
    
    return answer