a, b = map(int, input().strip().split(' '))
star = ""
for i in range(0, a):
    star+="*"

for i in range(0, b) :
    print(star)
    