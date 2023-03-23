colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
result_list=[]
result=int(1)

for i in range(0, 2) :
    color=input()
    for j in range(0,10) :
        if color==colors[j] :
            result_list.append(str(j))


color_str = ''.join(result_list)
color_result = int(color_str)

color=input()
for k in range(0,10) :
    if color==colors[k] :
        color_result*=(10**k)

print(color_result)