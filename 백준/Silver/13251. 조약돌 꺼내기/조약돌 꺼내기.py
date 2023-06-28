m = int(input())
stone_color = input().split()
stone_color = list(map(int, stone_color))
k = int(input())
total_sum = 0.0


for i in range(0, m) :
        stone_sum = 1.0
        for j in range (0, k) :
            a=stone_color[i]-j
            b=sum(stone_color)-j
            stone_sum *= (a/b)

        total_sum += stone_sum        

print(total_sum)


