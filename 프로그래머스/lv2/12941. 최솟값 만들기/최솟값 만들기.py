def solution(A,B):
    answer = 0
    a=[]
    b=[]
    
    for i in range(0, len(A)):
        a.append(A[i])
        b.append(B[i])
            
    count = len(B)-1
    a.sort()
    b.sort(reverse=False)
    
    for i in range(0, len(A)) :
        answer += a[i]*b[(count-i)]
    
    
    return answer