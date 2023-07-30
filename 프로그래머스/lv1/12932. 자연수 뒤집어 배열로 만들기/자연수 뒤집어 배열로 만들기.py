def solution(n):
    answer = []
    
    num= str(n)
    
    for i in range(len(num)-1, -1,-1) :
        answer.append(int(num[i]))    
    
    
    
    
    return answer