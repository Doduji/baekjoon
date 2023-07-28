def solution(n, control):
    answer = n
    
    for i in range(0, len(control)) :
        if control[i]=='w' :
            answer+=1
        elif control[i]=='s' :
            answer-=1
        elif control[i]=='d' :
            answer+=10
        else :
            answer-=10
    
    return answer