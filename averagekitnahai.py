# Average Kitna Hai
# Ek code likho jo kissi bhi list ke liye uss list ke do average ko output karta hai, 
# ki uss list mei odd numbers ka average aur even numbers ka average kitna hai.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
evensum=0
evencount=0
oddsum=0
oddcount=0
for i in elements:
    if i % 2 ==0:
        evencount=evencount+1
        evensum=evensum+1
    else:
        oddcount=oddcount+1
        oddsum=oddsum+i
evenavg=evensum//evencount
oddavg=oddsum//oddcount
print(evenavg,"is the average of all the even numbers present in the list")
print(oddavg,"is the average of all the odd numbers present in the list")