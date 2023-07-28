def solution(num_list):
    answer = []
    
    answer=list(num_list)
    
    if num_list[len(num_list)-1] > num_list[len(num_list)-2] :
        answer.append(num_list[len(num_list)-1]-num_list[len(num_list)-2])
    else :
        answer.append(num_list[len(num_list)-1]*2)
    
    
    return answer