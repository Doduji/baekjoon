def solution(emergency):
    answer = []
    
    s_eme = list(emergency)
    s_eme.sort(reverse=True)

    for i in range(0, len(emergency)) :
        for j in range(0, len(emergency)) :
            if (emergency[i])==(s_eme[j]) :
                answer.append(j+1)
    
    return answer