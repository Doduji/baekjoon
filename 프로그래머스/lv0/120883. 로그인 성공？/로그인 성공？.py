def solution(id_pw, db):
    answer = 'fail'
    
    id_check, pw_check= 0, 0
    
    for i in range(0, len(db)) :
        if id_pw[0]==db[i][0] :
            answer='wrong pw'
            if id_pw[1] == db[i][1] :
                answer = 'login'
            

    
    return answer