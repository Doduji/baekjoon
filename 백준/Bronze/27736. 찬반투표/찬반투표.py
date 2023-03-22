n = int(input())
app, rej, inv = 0, 0, 0 #통과 미통과 무효
result = []
result = list(map(int, input().split()))
   
for i in range(0, n) :
    if result[i]==1 :
        app+=1
    elif result[i]==(-1) :
        rej+=1
    else : 
        inv+=1

if inv >= (n/2) :
    print("INVALID")
elif app>rej :
    print("APPROVED")
else :
    print("REJECTED")


