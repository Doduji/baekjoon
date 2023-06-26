yt, yj = map(int, input().split())

while(1) :
    if (yt>=5):
        print("yj")
        break
    if(yj>=5):
        print("yt")
        break

    yj += yt 

    if (yt>=5):
        print("yj")
        break
    if(yj>=5):
        print("yt")
        break 

    yt+=yj
    
