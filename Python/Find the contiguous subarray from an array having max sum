n=[-2,1,-3,4,-1,2,1,-5,4]

# initialize start index end index and max_sum to first element in list
start,end,max_sum = n[0],n[0],n[0]

for i in range(len(n)):
    for j in range(len(n)):
        s = sum(n[i:j+1])
        if s > max_sum:
            start,end,max_sum=i,j,s

print(start,end,max_sum)
