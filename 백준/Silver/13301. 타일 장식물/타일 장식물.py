n = int(input())
#fibonacci = []
fir, sec = 0, 1
for i in range(0, n) :
#    fibonacci.append(sec)
    sum_num = fir+sec
    fir = sec
    sec = sum_num

#fibonacci.sort(reverse=True)
#print(fibonacci)
#print((fibonacci[0]*2+fibonacci[1])*2)

print((fir+sec)*2)