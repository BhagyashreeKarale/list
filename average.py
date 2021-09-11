# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# sum=0
# count=0
# for i in numbers:
#     sum=sum+i
#     count=count+1
# print(sum/count,"is the average of the list")
###############################################################################################################################
#with user input
sum=0
num=int(input("Enter number of values"))
count=0
for i in range(num):
    ui=int(input("enter value"))
    sum=sum+ui
    count=count+1
print(sum,"is the sum of the values entered")
avg=sum/count
print(avg,"is the average of the values entered")

