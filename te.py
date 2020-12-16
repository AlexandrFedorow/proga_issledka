def convert(x):
    s = 0
    for i in range(len(x)):
        if x[i] == 'a':
            s += 10
        elif x[i] == 'b':
            s += 11
        elif x[i] == 'c':
            s += 12
        elif x[i] == 'd':
            s += 13
        elif x[i] == 'e':
            s += 14
        elif x[i] == 'f':
            s += 15
        else:
            s += int(x[i])
    return s


ctr = 0
for i in range(128, 2048, 1):
    a = hex(i)
    b = hex(i*2)

    a = a[2::]
    b = b[2::]

    if len(a) == 3 and len(b) == 3 and '5' in a:
        sa = convert(a)
        sb = convert(b)
        if sa == sb:
            print(b, ' ', a)
            ctr += 1
print(ctr)