li = [1, 5, 3, 2]
count = []
for i in range(len(li)):
    for j in range(i+1, len(li)):
        s = li[i] + li[j]
        if s in li and s not in count:
            count.append(s)
print(len(count))
