x = int(input())
x_copy = x
stick = [64, 32, 16, 8, 4, 2, 1]
plus_stick ,count_stick = 0, 0

for i in range (0, len(stick)) :
    if x_copy >= stick[i] :
        plus_stick += stick[i]
        x_copy -= stick[i]
        count_stick += 1
    if x==plus_stick :
        break


print(count_stick)
