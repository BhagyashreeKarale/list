#Q: Given two arrays, 1,2,3,4,5 and 2,3,1,0,5 find which numbers are not present in the second array.

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i)
print(list3)
        

# Output: [4, 5]
#################################################################################################################
# Report Card
# Iss list ko dekhein:

marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]

# # Yeh kisi student ke peechle teen saal ke marks hai. 
# # Aap ko teeno saalo, ke sab subjects ke marks ka total calculate karna hai.
# # Jaise uppar di hui nested list ka sum - 1142 aayega.
sum=0
for i in marks:
    for j in i:
        sum=sum+j
print(sum)
######################################################################################################################
#avg of every year
marks = [[78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]]
# #Yeh kisi student ke peechle teen saal ke marks hai. 
# # Aap ko jitne bhi saal hai, har saal ke average marks print karne hai. 
# # Jaise, uppar wali list ka output yeh hona chahiye:
for i in marks:
    sum=0
    count=0
    for i in i:
        sum=sum+i
        count=count+1
    avg=sum/count
    print(avg)
print("Average of every year in sequence are as above")
###########################################################################################################################
#pairs
#How to find all pairs in an array of integers whose sum is equal to the given number?

number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
for i in  n:
    num=int(i)
    for j in n:
        if int(j)+num==number:
            print(i,j)

marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + int(marks[counter])
    counter = counter + 1
print(total_marks)