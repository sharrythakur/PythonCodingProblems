li=[3,5,7,4,5,6,8,33,4,33]

# sol 1
s = set(li)
print(sorted(s)[-2])

# sol 2

li2 = []
while li:
    minimum = li[0]
    for i in li:
        if i < minimum:
            minimum = i
    li2.append(minimum)
    li.remove(minimum)
print(li2)
