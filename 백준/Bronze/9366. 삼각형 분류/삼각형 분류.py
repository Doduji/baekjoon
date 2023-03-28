n = int(input())

case = []

for i in range(0, n) :
    triangle= list(map(int, input().split()))
    
    if triangle[0] == triangle[1] == triangle[2] :
        case.append("equilateral")
 
    elif triangle[0]>=(triangle[1]+triangle[2]) or triangle[1]>=(triangle[0]+triangle[2]) or triangle[2]>=(triangle[1]+triangle[0]) :
        case.append("invalid!")
    
    elif triangle[0] == triangle[1] != triangle[2] or triangle[0] != triangle[1] == triangle[2] or triangle[0]==triangle[2]!=triangle[1] :
        case.append("isosceles")

    else :
        case.append("scalene")
    

for i in range(0, n) :
    print("Case #%d: %s" %(i+1, case[i]))
