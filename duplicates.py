n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]   
print("Duplicate elements in given nay: ");      
for i in range(0, len(n)):    
    for j in range(i+1, len(n)):    
        if(n[i] == n[j]):    
            print(n[j])#this will print all duplicate values as number of times as they have occured.ex it wil print 
# count=0
# counter=0
# sum=0
# dup=[]
# while count<len(n):
#     i=n[count]
#     c2=0
#     con2=1
#     while c2<len(n):
#         j=n[con2]
#         if i == j:
#             sum=sum+1
#             if sum>=1:
#                 if j not in dup:
#                     dup.append(j)
#                 con2=con2+1
#         con2=con2+1
#     c2=c2+1
# count=0
# counter=0
# while count<len(n):
#     i=n[count]
#     con2=1
#     while con2<len(n):
#         j=n[con2]
#         sum=0
#         if i == j:
#             sum=sum+1
#             if sum>1:
#                 print(j)
#             con2=con2+1
#         con2=con2+1
    # count=count+1

# count=0
# counter=0
# while count<len(n):
#     i=n[count]
#     con2=0
#     while con2<len(n):
#         j=n[con2]
#         if i == j:
#             counter=counter+1
#             if counter>1:
#                 print(j)
#                 count=count+1
#         con2=con2+1
#     count=count+1

    
# for i in range(len(n)):
#     for j in range(len(n)):
#        if n[i] == n[j]:
#             count=count+1
#     if count>1:
#         print(i)
        
# print(dlist)
# for i in n:
#     if i not in dlist:
#         dlist.append(i)
# print(dlist)
# for i in n:
#     if i9 in n and i in dlist:
#         dup.append(i)
#         if i not in dup:
#             print(i)
 
# n = [19, 17, 12, 17, 17, 18, 97, 10, 17, 14, 12, 19, 17, 12, 13, 11, 97]#[19, 17, 12, 18, 10, 14, 13, 11]
# ulist=[]
# for i in n:
#     if i not in ulist:
#         ulist.append(i)
# print(ulist,"These are single occurences every value present in the list")
# dlist=[]
# flist=[]
# for i in range(len(n)):
#     x=n[i]
#     count=0
#     for j in n:
#         if j == x:
#             count=count+1
#             if count>1:
#                 dlist.append(j)
#                 count=0
#                 for i in dlist:
#                     if i not in flist:
#                         flist.append(i)
# print(flist,"These are the values which have more than one occurence in the list")

# a=[]
# b=[]
# x=[]
# i=0
# while i <len(n):
#     # print(n[i])
#     if n[i] not in a:
#         a.append(n[i])
#     else:
#         b.append(n[i])
#     j=0
#     while j<len(b):
#         if b[j] not in x:
#             x.append(b[j])
#         j+=1
#     i+=1
# print(x)
#######################################################################################################
#practice
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# u = []
# d = []
# for k in range (len(n)):
#     if n[k] not in u:#this will check for unique values
#         u.append(n[k])
#         count=0
#         for i in range (len(n)):
#             if n[k] not in d:#here we can also write n[i] in place of n[k]#we are 
#                 if n[k] == n[i]:
#                     count=count+1
#                     if count>1:
#                         d.append(n[k])#this is the list of elements occured more than one time
# print(d,"these are values which have more than one occurence")
