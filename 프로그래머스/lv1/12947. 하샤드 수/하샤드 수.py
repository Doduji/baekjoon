def solution(x):
    answer = True
    org = x
    n_list = []

    div_ten =  i = 10000

    for i in range(0, 5) :
        if (int(x/div_ten))!=0 : 
            a=int(x/div_ten)
            n_list.append(a)
            x= x-(a*div_ten)

        div_ten = div_ten / 10


    if(org%sum(n_list))==0 : 
        answer = True
    else : 
        answer = False
    
    
    
    return answer