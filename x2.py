a=[1,2,[3,4],5,6,[7,8],[9],10]
for k in range(len(a)):
    if type(a[k]) == list:
        for i in range(len(a[k])):
            if a[k][i] % 3 == 0 and a[k][i]!=0 and a[k][i]!=1:
                a[k][i]="yes"
    else:
        if a[k] % 3 == 0 and a[k]!=0 and a[k]!=1:
            a[k]="yes"
print(a)