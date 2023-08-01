def solution(d, budget):
    answer = 0
    num=[]
    
    for i in range(0, len(d)) :
        num.append(d[i])
        
        
    num.sort(reverse=False)
        
    buy =0
    
    for i in range(0, len(d)) :
        buy+=num[i]
        if budget<buy :
            buy_=num[i]
            break
        answer+=1
    
    
    
    return answer