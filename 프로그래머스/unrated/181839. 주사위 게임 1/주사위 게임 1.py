def solution(a, b):
    answer = 0
    
    if a%2!=0 and b%2!=0 :
        answer = a*a +b*b
    elif a%2==0 and b%2==0 :
        answer = a-b
        if answer<0 :
            answer*=-1
    else :
        answer = 2*(a+b)
    
    return answer