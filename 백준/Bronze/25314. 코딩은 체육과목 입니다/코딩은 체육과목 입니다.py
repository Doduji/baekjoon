n = int(input())
n = int(n/4)
long_list = []

for i in range(0, n) :
    long_list.append("long ")

long_list.append("int")

long_list=''.join(s for s in long_list)

print(long_list)