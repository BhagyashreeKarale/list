#Q: How to find all pairs in an array of integers whose sum is equal to the given number?
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19,30]
for i in n:
    num=int(i)
    for i in n:
        if int(i)+num==number:
            print(i,num)
print("These pairs sum up to 30")
#without duplicate values
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19,30]
u=[]
for i in n:
    for k in n:
        if int(k)+int(i)==number:
            n.remove(k)
            print(i,k)
print("These pairs sum up to 30")
        