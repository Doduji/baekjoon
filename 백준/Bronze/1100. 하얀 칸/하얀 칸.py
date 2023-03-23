chess = []
count = 0

for i in range(0, 8) :
    line = []
    chess_obj = input()
    line = list(chess_obj)
    chess.append(line)

for j in range(0, 8) :
    for k in range(0, 8) :

        if ((j+k)%2)==0 and chess[j][k]=='F' :
            count+=1

print(count)
