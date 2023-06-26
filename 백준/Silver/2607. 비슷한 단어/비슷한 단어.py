a = int(input())
word = []
same = 0
 
for i in range(0, a) :
    word.append(input())

base = list(word[0])

for i in range(1, a) :
    current = list(word[i])
    count=0
    
    if (len(current)-len(base)) < (-1) :
        continue
    if (len(current)-len(base)) > 1 :
        continue

    for j in range(0, len(base)) :
        if base[j] in current :
            current.remove(base[j])
            count += 1 
    
    if (len(list(base)) - count) > 1 :
        #print("?")
        continue

    if len(current) == 0 :
        #print(i)
        same+=1
    elif len(current) == (-1) :
        #print(i)
        same+=1
    elif len(current) == 1 :
        #print(i)
        same+=1
    else :
        continue

print(same)

