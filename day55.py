r=[11,12,13,50]
for i in range(1,4):# or (0,3)
    if r[0]>r[i]:
        r[0]=r[i]
print(f'{r[0]} is the smallest number')