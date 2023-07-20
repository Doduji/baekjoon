def solution(numbers, k):
    answer = 0
    
    count=1
    while((k*2)>(count*len(numbers))) :
        count+=1

    num_list=[]
    for i in range(0, count) :
        for j in range(0, len(numbers)):
                num_list.append(numbers[j])
    answer=num_list[(k*2)-2]
    
    return answer