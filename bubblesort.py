a=[1,6,3,9,34,89,80,4,2,6,30]
n=len(a)
for i in range(n):
    if i==n-1:
        print(a[j])
    else:
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
        print(a[j+1])   
#######################################################################################################
#with user input:
ui=int(input("Enter the number of values you want to enter"))
nlist=[]
for i in range(ui):
    num=input("Enter value")
    nlist.append(num)
n=len(nlist)
for i in range (n):
    if i==n-1:
        print(nlist[j])
    else:
        for j in range(n-1-i):
            if nlist[j]>nlist[j+1]:
                temp=nlist[j]
                nlist[j]=nlist[j+1]
                nlist[j+1]=temp
        print(nlist[j+1])
############################################################################################################
#another way without using if else
a=[1,6,3,9,34,89,80,4,2,6,30]
temp=0
flist=[]
for k in range(len(a)-1):#this will run only length if the list-1 number of times as if the rest of the elements are at their place the last one will automatically be at its's place
    for i in range(len(a)-k-1):#this will compare the respective element excluding the proper placed ones 
        if a[i]>a[i+1]:#here if we change sign from > to < it will print ascending list
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
    flist.append(a[i+1])#this will apppend the largest element of the list*note;list is updated in every round.first round :largest element of whole list,second round:largest element of the list excluding the largest element found in the first list..and so on 
flist.append(a[i])#this is necessary as the last element will not get printed without this
print(flist)
#here append is only needed when you take another list.#then you have to print that new list in the print function.
#if you want to update the existing list,you don't have to use append
#just print the existing list outside the loop
    
    
