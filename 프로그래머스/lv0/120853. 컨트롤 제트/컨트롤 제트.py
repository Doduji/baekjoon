def solution(s):
    answer = 0
    
    div = list(s.split())

    for i in range(0, len(div)) :
        if div[i]=="Z" :
            answer -= int(div[i-1])
        else : 
            answer += int(div[i])
    
    
    return answer