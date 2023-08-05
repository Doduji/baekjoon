def solution(k, m, score):
    answer = 0
    apple = score[:]
    apple.sort(reverse=True)


    count = int(len(apple)/m)
    c = count-1

    ind = m-1



    for i in range(0, count) :       
        answer+=apple[ind]*m
        ind+=m
    
    return answer