#Selection Sort

li = [6,3,8,5,66,8,44,2,66]

for i in range(len(li)):
    min_ele_index = i
    for j in range(i+1,len(li)):
        if(li[min_ele_index] > li[j]):
            min_ele_index = j

    li[i], li[min_ele_index] = li[min_ele_index], li[i]

print(li)
