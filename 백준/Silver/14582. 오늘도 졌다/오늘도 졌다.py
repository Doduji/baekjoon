away = list(map(int, input().split()))
home = list(map(int, input().split()))
turn_around=False
v=0 #1일땐 역전패 가능, 0일땐 불가능

away_score, home_score = 0,0

for i in range(0, 9) :
    away_score += away[i]

    if away_score > home_score :
        v=1
    elif away_score <= home_score :
        v=0

    home_score += home[i]

    #print("%d : %d"%(i,v))

   # print(v==1 and away_score < home_score)
    if v==1 and away_score < home_score :
        turn_around = True
    

if turn_around==True :
    print("Yes")
else :
    print("No")

