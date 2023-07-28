def solution(my_string, is_prefix):
    answer = 1
    
    if len(my_string) < len(is_prefix) :
        count=len(my_string)
    else :
        count=len(is_prefix)

    for i in range(0, count):
        if is_prefix[i]!=my_string[i] :
            answer=0
    
    if count==len(my_string) :
        answer=0
    
    
    return answer