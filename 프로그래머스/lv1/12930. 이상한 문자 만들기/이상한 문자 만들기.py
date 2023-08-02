def solution(s):
    answer = ''
    count=1
    for i in range(0, len(s)) :
        if s[i]==' ' :
            answer += ' '
            count=1
            continue
        elif count%2!=0 :
            answer+=s[i].upper()
            count+=1
        else :
            answer+=s[i].lower()
            count+=1
        
    return answer