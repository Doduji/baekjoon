
friend_list = []

while True :
    a, b = map(int, input().split())
    if a==0 and b==0 :
        break
    friend_list.append(a+b)

for i in friend_list :
    print(i)