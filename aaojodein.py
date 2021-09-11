#Ek code likho jo kissi bhi list ke liye uss list ke do sum ka output karta hai, 
# ki uss list mei odd numbers ka sum aur even numbers ka sum kitna hai.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
esum=0
osum=0
for i in elements:
    if i % 2 == 0:
        esum=esum+i
    else:
        osum=osum+i
print(esum,"is the sum of all the even numbers present in the list")
print(osum,"is the sum of all the odd numbers present in the list")
##############################################################################################################
#with user inputed list
counter=1
ui=int(input("Enter the total numbers of value"))
esum=0
osum=0
while counter<=ui:
    num=int(input("Enter value"))
    if num % 2 == 0:
        esum=esum+num
    else:
        osum=osum+num
    counter=counter+1
print(esum,"is the sum of all the even numbers present in the list")
print(osum,"is the sum of all the odd numbers present in the list")

