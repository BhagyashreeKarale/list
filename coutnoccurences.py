# Count Occurences
# Occurences - occur shabd se bana hai, jiska matlab hota hai, ki kitni baar aata hai.

# Sample List
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]

# Sample List ka Output:
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]

# a - 6 times
# n - 3 times
# t - 2 times
# x - 2 times
# u - 1 times
# g - 1 times

# Humei char_list mei jo bhi characters hai, unki occurences count karni hai, 
# aur ek nested list mei save karni hai, 
# phir uss nested list ko use kar kar jo output hai, woh print karna hai.

# Edge Case
# char_list = []

# Solution
# []
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# ulist=[]
# flist=[]
# for i in range (len(char_list)):
#     j=0
#     count=0
#     for j in range(len(char_list)):
#         if char_list[i]==char_list[j]:
#             count=count+1
#     if char_list[i] not in ulist:
#         ulist.append(char_list[i])
#         print(char_list[i],"-",count,"times")
############################################################################################################
#practice
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
blist=[]
ulist=[]
for k in range (len(char_list)):
    x=char_list[k]
    if x not in ulist:
        ulist.append(x)
        count=0
        slist=[]
        for i in range(len(char_list)):
            if char_list[i] == x:
                count=count+1
    # slist.append(x)#instead of using append twice you can get the same result by using extend once.make sure extend parentheses has a list.
        slist.extend([x,count])
        blist.append(slist)
print(blist)