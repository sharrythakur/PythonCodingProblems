first = 1
second = 1
third = first + second

print(first,second, end=' ')
for i in range(1,10):
    third = first + second
    first = second
    second = third
    print(third,end=' ')
