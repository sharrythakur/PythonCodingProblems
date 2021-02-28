
# Insertion Sort

arr = [14, 25, 33, 4, 51, 6]

for i in  range(1,len(arr)):
    temp = arr[i]
    j = i-1
    while(j>=0 and arr[j]>temp):
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = temp
print(arr)


