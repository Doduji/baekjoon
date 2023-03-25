number = list(map(int, input().split()))
check = True
mul = 0

while check :
    mul += 1
#    print(mul)
    check_num = [0, 0, 0, 0, 0]
    for i in range(0, len(number)) :
        if (mul%number[i]) == 0 :
            check_num[i] = 1
    if sum(check_num) > 2 :
        check = False
       # print("check = false %d" % mul)
    
print(mul)
        



