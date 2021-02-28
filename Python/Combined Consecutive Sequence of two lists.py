li = [1, 4, 6, 5]
li1 = [2, 7, 8, 9]

max_n = max(li) if max(li)>max(li1) else max(li1)
min_n = min(li) if min(li)<min(li1) else min(li1)
flag = True
for i in range(min_n, max_n+1):
    if i not in li and i not in li1:
        flag = False
        break
print(flag)
