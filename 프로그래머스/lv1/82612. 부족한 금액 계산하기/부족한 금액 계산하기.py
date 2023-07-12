def solution(price, money, count):
    answer = 0


    for i in range(0, count) :
        money -= price*(i+1)
    
    answer=(money)*(-1)
    
    if money>=0 :
        answer=0
    
    return answer