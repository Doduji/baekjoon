def solution(n):
    answer = 0
    n_list = []

    div_ten =  i = 100000000

    for i in range(0, 9) :
        if (int(n/div_ten))!=0 : 
            a=int(n/div_ten)
            n_list.append(a)
            n= n-(a*div_ten)

        div_ten = div_ten / 10

        
    answer = sum(n_list)
    return answer