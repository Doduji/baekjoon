n = int(input())
hippo_list=[]
for i in range(0, n) :
    hippo_list.append(input())
    hippo=list(set(hippo_list))

print(n-len(hippo))
