pyramid = ''
for i in range(10):
    for k in range(i, -1, -1):
        pyramid += str(k)
    pyramid += ('\n')
print(pyramid)
