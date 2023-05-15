n = int(input())
customer = []
count_list=[]

for i in range(0, n) :
    size = int(input())
    customer.append(size)

rm_set=list(set(customer))

for i in range(0, (len(rm_set))) :
    rm_num = rm_set[i]
    count=1
#    count_sample = []
    sample_list = list(customer)
    while rm_num in sample_list :
        sample_list.remove(rm_num)

    for j in range(1, (len(sample_list))) :

        if (sample_list[j-1]) == (sample_list[j]):
            count+=1
            count_list.append(count)
            
        if(sample_list[j-1]) != (sample_list[j]) :
            count_list.append(count)
            count = 1
     
#        count_list.append(max(count_sample))

print(max(count_list))


