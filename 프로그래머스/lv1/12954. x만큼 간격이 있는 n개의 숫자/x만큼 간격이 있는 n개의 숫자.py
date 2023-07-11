def solution(x, n):
    copy_x = x
    answer=[]
    for i in range(0, n) :
        answer.append(copy_x)
        copy_x= copy_x+x

    return answer