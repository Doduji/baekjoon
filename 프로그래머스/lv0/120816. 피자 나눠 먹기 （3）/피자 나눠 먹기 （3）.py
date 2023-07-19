def solution(slice, n):
    answer = 1
    pizza = slice
    while(pizza<n) :
        pizza+= slice
        answer+=1
    
    
    return answer