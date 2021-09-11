numbers=[31,493,392,94,24,5,6,]
min=0
for i in range(len(numbers)-1):
    for k in range(len(numbers)-1-i):
        if numbers[k]<numbers[k+1]:
            min=numbers[k]
            numbers[k]=numbers[k+1]
            numbers[k+1]=min
print(i,"is the minimun value present in a list")