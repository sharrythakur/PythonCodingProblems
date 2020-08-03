a = [6, 4, 3, 7, 10, 45, -1]
b = [1, 2, 3, 7, 6, -1]
result = []

def find_common(a, b):
    n = a if len(a) < len(b) else b
    n.sort()
    for i in range(n[0], n[-1]+1):
        if i in a and i in b:
            result.append(i)
    return result


print(find_common(a, b))
