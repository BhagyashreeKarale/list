#Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
diff=[]
for i in list1:
    if i not in list2:
        diff.append(i)
print(diff,"These values are of list1 which aren't present in list2")