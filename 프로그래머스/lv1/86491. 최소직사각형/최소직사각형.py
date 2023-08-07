def solution(sizes):
    answer = 0
    
    x, y = 0,0
    
    for i in range(0, len(sizes)) :
        if (sizes[i][0] < sizes[i][1]) :
            k = sizes[i][0]
            j = sizes[i][1]
        else :
            j = sizes[i][0]
            k = sizes[i][1]
        
        if j > x :
            x=j
        if k > y :
            y=k

    
    answer=x*y
    
    return answer