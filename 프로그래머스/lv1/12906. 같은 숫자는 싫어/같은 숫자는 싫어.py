def solution(arr):
    answer = []
    
    for i in range(0, len(arr)):
        if arr[i-1]==arr[i] and i!=0 :
            continue
        else :
            answer.append(arr[i])
    
    
    return answer