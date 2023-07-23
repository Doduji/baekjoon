def solution(score):
    answer = []
    avg_list = []

    for i in range(0, len(score)) :
        avg_list.append((score[i][0]+score[i][1])/2)

    rank_list = [0]*len(avg_list)
    max_score = max(avg_list)

    
    rank = 1
    i=0
    while(len(avg_list)-1>=i) :
        count=0
    
        for j in range(0, len(avg_list)):

            if avg_list[j]==max_score :
                rank_list[j]=rank
                avg_list[j] = -1
                count+=1

            
        rank+=count
        i+=count
        max_score=max(avg_list)    
    
    
    answer=rank_list
    return answer