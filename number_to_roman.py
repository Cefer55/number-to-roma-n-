s = int(input())
s = list(str(s))
symbol = ["I", "V", "X", "L", "C", "D", "M", "V̅", "X̅", "L̅", "C̅", "D̅", "M̅"]
value = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
a = []

m = len(s)
for i in range(0, len(s)):
    s[i] = int(s[i])
    m -= 1
    a.append((s[i]) * (10 ** m))

e = []
t = []
for i in range(0, len(a)):
    y = 10**(len(str(a[i]))-1)
    x = a[i] // y

    if x == 5:
        e.append(1)
        t.append(a[i])
        continue
    elif x < 4:
        e.append(x)
        t.append(y)
    elif x > 5 and x < 9:
        e.append(1)
        e.append(x - 5)
        t.append(5 * y)
        t.append(y)
    elif x == 4 or x == 9:
        e.append(1)
        e.append(1)
        t.append(y)
        t.append((x + 1) * y)

p = ""
for i in range(0, len(t)):
    for j in range(0, len(value)):
        if t[i] == value[j]:
            p = p + (symbol[j] * e[i])


print(p)