def solution(num_list):
    answer = 1
    
    sum_num=0
    mul_num=1
    
    for i in range(0, len(num_list)):
        sum_num+=num_list[i]
        mul_num*=num_list[i]
    
    if mul_num>(sum_num*sum_num) :
        answer=0
    
    
    return answer