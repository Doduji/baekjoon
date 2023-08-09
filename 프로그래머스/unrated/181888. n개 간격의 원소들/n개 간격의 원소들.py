def solution(num_list, n):
    answer = []

    count=n
    for i in range(0, len(num_list)) :
        
        if count==n :
            answer.append(num_list[i])
            count=0
        count+=1
    
    return answer