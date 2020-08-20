a = []
for i in range(10):
    for k in range(i,-1,-1):
        a.append(str(k))
    a.append('\n')
pyr  = ''
for i in a:
    pyr += i
print(pyr)
