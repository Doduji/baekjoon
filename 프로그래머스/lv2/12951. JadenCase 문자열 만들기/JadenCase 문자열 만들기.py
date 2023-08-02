def solution(s):
    answer = ''
    count=0
    for i in range(0, len(s)) :
        if s[i]==' ' :
            answer += ' '
            count=0
        elif count==0 :
            answer+=s[i].upper()
            count+=1
        else :
            answer+=s[i].lower()
    
    return answer