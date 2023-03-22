
m=int(input())

cup = ["","ball", "", ""] 

for count in range(m) :
    fir, sec = input().split()
    fir, sec = int(fir), int(sec)

    if cup[fir]=="ball" or cup[sec]=="ball" :
        cup[0]=cup[fir]
        cup[fir]=cup[sec]
        cup[sec]=cup[0]
        cup[0]=""

for result in range(len(cup)) :
    if cup[result] == "ball" :
        print(result)
