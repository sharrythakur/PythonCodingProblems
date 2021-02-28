a=[3,5,6,9,12,14,18,20,25,28]
b=[30,32,34,36,38,40,42,44,46,48]

min = b[0] if a[0] > b[0] else a[0]
max = a[-1] if a[-1] > b[-1] else b[-1]
c = []
for i in range(min, max+1):
    if i in a or i in b:
        c.append(i)

print(c)
