def solution(cards1, cards2, goal):
    answer = ''
    
    count1, count2 = 0, 0 
    
    for i in range(0, len(goal)):
        if goal[i]==cards1[count1] :
            if count1<len(cards1)-1 :
                count1+=1
        elif goal[i]==cards2[count2] :
            if count2<len(cards2)-1 :
                count2+=1
        else :
            i=0
            break
    
    if len(goal)-1==i :
        answer='Yes'
    else :
        answer='No'
    
    return answer