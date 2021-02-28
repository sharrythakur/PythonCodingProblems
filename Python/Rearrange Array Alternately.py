arr = [1, 2, 3, 4, 5, 6]

flag= -1
for i in range(0, len(arr), 2):
    arr.insert(i,arr[flag])
    arr.pop()
print(arr)
