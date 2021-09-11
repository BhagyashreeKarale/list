#ascending
a=[21,4,7,9,2,8,5,12]
for i in range(len(a)):
    if a[i] % 2 == 0:
        for s in range (len(a)):
            for k in range ((len(a))-s):
                if a[k] % 2 == 0:
                    if a[i]<a[k]:
                        temp=a[i]
                        a[i]=a[k]
                        a[k]=temp
print(a)
#descending
a=[21,4,7,9,2,8,5,12]
for i in range(len(a)):
    if a[i] % 2 == 0:
        for s in range (len(a)):
            for k in range ((len(a))-s):
                if a[k] % 2 == 0:
                    if a[i]>a[k]:
                        temp=a[i]
                        a[i]=a[k]
                        a[k]=temp
print(a)
                    
                                      
                    