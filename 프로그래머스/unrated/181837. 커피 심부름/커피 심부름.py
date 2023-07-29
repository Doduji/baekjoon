def solution(order):
    answer = 0
    
    for i in range(0, len(order)) :
        if "cafelatte" in order[i] :
            answer+=5000
        else :
            answer+=4500
    
    
    return answer