def solution(balls, share):
    answer = 0
    up=1
    down=1
    
    for i in reversed(range(share+1, balls+1)) :
        up*=i


    for i in range(1, (balls-share)+1) :
        down*=i
        
    answer = int(up/down)
    
    return answer