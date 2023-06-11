def ddd(a, b):
    res = []
    for i in range(ord(a) + 1, ord(b)):
        res.append(chr(i))

    return res


x = input()
y = input()

result = ddd(x, y)
print(" ".join(result))