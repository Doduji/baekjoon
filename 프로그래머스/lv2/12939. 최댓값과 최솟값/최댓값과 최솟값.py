def solution(s):
    answer = ''
    
    num = list(s.split())
    n = []
    
    for i in range(0, len(num)) :
        n.append(int(num[i]))
        
    n.sort()
    
    answer =  str(n[0]) + " " + str(n[len(n)-1])
    
    return answer