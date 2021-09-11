# statues=[6,2,3,8]
# # flist=statues.copy()
# n=len(statues)
# for j in range (n-1):
#     for i in range (n-1-j):
#         if statues[i]>statues[i+1]:
#             temp=statues[i]
#             statues[i]=statues[i+1]
#             statues[i+1]=temp
# # print(statues)#2,3,6,8*this part is for getting the values in ascending order
# flist=statues.copy()
# for i in range ((len(statues))-1):
#     if statues[i]+1==statues[i+1]:
#         statues[i]=statues[i+1]
#     else:
#         dif=statues[i+1]-statues[i]
#         for k in range(dif-1):
#             flist.append(statues[i]+1)
#             statues[i]=statues[i]+1
# # print(flist)#this will give the unordered list.now we again have to arrange this in an ascending order
# n=len(flist)
# for a in range(n-1):
#     for b in range(n-1-a):
#         if flist[b]>flist[b+1]:
#             temp=flist[b]
#             flist[b]=flist[b+1]
#             flist[b+1]=temp
# print(flist)#this will be the final list
# ######################################################################################################33
# #with user input
# # ninput=int(input("Enter the number of values you want to enter"))
# # statues=[]
# # for i in range(ninput):
# #     ninput=int(input("Enter the value"))
# #     statues.append(ninput)
# # flist=statues.copy()
# # n=len(statues)
# # for j in range (n-1):
# #     for i in range (n-1-j):
# #         if statues[i]>statues[i+1]:
# #             temp=statues[i]
# #             statues[i]=statues[i+1]
# #             statues[i+1]=temp
# # # print(statues)#2,3,6,8
# # for i in range ((len(statues))-1):
# #     if statues[i]+1==statues[i+1]:
# #         statues[i]=statues[i+1]
# #     else:
# #         dif=statues[i+1]-statues[i]
# #         for k in range(dif-1):
# #             flist.append(statues[i]+1)
# #             statues[i]=statues[i]+1
# # # print(flist)
# # n=len(flist)
# # for a in range(n-1):
# #     for b in range(n-1-a):
# #         if flist[b]>flist[b+1]:
# #             temp=flist[b]
# #             flist[b]=flist[b+1]
# #             flist[b+1]=temp
# # print(flist)
# #######################################################################################################
# #practice
# statues=[6,2,3,8]
# # flist=statues.copy()
# n=len(statues)
# for j in range (n-1):
#     for i in range (n-1-j):
#         if statues[i]>statues[i+1]:
#             temp=statues[i]
#             statues[i]=statues[i+1]
#             statues[i+1]=temp
# # print(statues)#2,3,6,8*this part is for getting the values in ascending order
# flist=statues.copy()
# for i in range (len(statues)-1):
#     if statues[i]+1==statues[i+1]:
#         statues[i]=statues[i+1]
#     else:
#         dif=statues[i+1]-statues[i]
#         for k in range(dif-1):#it is not in the range of dif it is in the range dif -1 as if we take dif it will print the last value which is already present in the list
#             flist.append(statues[i]+1)
#             statues[i]=statues[i]+1
# # print(flist)
# for k in range (len(flist)-1):
#     for i in range(len(flist)-1-k):
#         if flist[i]>flist[i+1]:
#             temp=flist[i]
#             flist[i]=flist[i+1]
#             flist[i+1]=temp
# print(flist)
        
#another way to do this is to find the largest among the list and then print all in range of that number

statues=[6,2,3,8]
max=0
for i in statues:
    if i > max:
        max=i
for k in range(1):
    for j in range (len(statues)-1):
        if statues[j] < statues[j+1]:
            min=statues[j]
            statues[j]=statues[j+1]
            statues[j+1]=min        
for l in range (j,i+1):
        print(l)



statues=[6,2,3,8]
max=0

for i in statues:
    if i > max:
        max=i
for j in range (len(statues)-1):
    if statues[j] < statues[j+1]:
        min=statues[j]
        statues[j]=statues[j+1]
        statues[j+1]=min
statues[j+1]=min
for l in range (min,max+1):
        print(l)

