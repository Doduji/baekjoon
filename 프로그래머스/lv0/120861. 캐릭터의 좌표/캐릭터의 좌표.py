def solution(keyinput, board):
    answer = [0,0]
    
    for i in range(0, len(keyinput)) :
        if keyinput[i]=="up" and (int(board[1]/2)>answer[1]) :
            answer[1]+=1
        elif keyinput[i]=="down" and (int(0-board[1]/2)<answer[1]) :
            answer[1]-=1
        elif keyinput[i]=="right" and (int(board[0]/2)>answer[0]) :
            answer[0]+=1
        elif keyinput[i]=="left" and (int(0-board[0]/2)<answer[0]) :
            answer[0]-=1
 
    return answer
