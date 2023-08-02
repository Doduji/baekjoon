def solution(s):
    answer = True
    count=0
    
    for i in range(0, len(s)):
        if count<0 :
            return False
        if s[i] =="(" :
            count+=1
        else :
            count-=1
    
    if count==0 :
        return True
    else :
        return False