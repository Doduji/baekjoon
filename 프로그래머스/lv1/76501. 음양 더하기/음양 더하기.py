def solution(absolutes, signs):
    answer = 123456789
    
    result_list = []

    for i in range(0, len(absolutes)):
        if signs[i]==False :
            result_list.append(0-absolutes[i])
        else :
            result_list.append(absolutes[i])

    answer = sum(result_list)
    
    return answer