def solution(n):
    answer = ''
    watermelon = []
    if (n%2)==0 :
        flag=False
    else : 
        flag=True
    for i in range(0, int(n/2)) :
        watermelon.append("수박")
    if flag :
        watermelon.append("수")
    answer=''.join(s for s in watermelon)
        
    return answer