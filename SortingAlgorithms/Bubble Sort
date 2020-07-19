arr = [14, 25, 33, 4, 51, 6]

for i in range(len(arr)-1):
    flag = 0
    for j in range(len(arr)-1-i):
        if(arr[j]>arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            flag = 1
    if flag == 0:
        break
print(arr)
