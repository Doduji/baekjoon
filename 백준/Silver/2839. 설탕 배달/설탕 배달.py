n=int(input())
c5, c3 = 0, 0

sugar=False

if (n%3)==0 and n<15:
    print(int(n/3))
    n=0
    sugar=True


while n>=5 :
    n-=5
    c5+=1
    if (n%3)==0 and n<15:
        print(int(n/3)+c5)
        n=0
        sugar=True
        

while n>=3 :
    n-=3
    c3+=1

if (c5!=0 or c3!=0) and n==0 and sugar!=True:
    print(c5+c3)
    
elif n!=0 :
    print(-1)


