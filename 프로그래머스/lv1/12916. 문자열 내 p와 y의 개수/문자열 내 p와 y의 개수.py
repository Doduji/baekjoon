def solution(s):
    answer = True
    p_count, y_count=0,0
    for i in range(0, len(s)) :
        if s[i]=='p' or s[i]=='P' :
            p_count+=1
        elif s[i]=='y' or s[i]=='Y' :
            y_count+=1
            
    if p_count==y_count :
        return True
    else :
        return False