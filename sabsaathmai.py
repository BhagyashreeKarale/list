# Ek code likho jo kisi bhi list ke liye yeh output karta hai, 
# ki uss list mei odd numbers, even numbers aur sab numbers ka:
# count
# sum
# average
# print aaye.

# Sample Input
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

# Sample Output
# odd numbers ka count .... hai 
# even numbers ka count .... hai 
# saare numbers ka count .... hai 
# odd numbers ka sum .... hai 
# even numbers ka sum .... hai 
# saare numbers ka sum .... hai 
# odd numbers ka average .... hai 
# even numbers ka average .... hai 
# saare numbers ka average .... hai
ocount=0
ecount=0
nsum=0
esum=0
osum=0
ncount=0
for i in elements:
    ncount=ncount+1
    nsum=nsum+i
    if i % 2 == 0:
        ecount=ecount+1
        esum=esum+i
    else:
        ocount=ocount+1
        osum=osum+i
navg=nsum/ncount
eavg=esum/ecount
oavg=osum/ocount
print("There are","total",ncount,"numbers")
print("Sum of all the numbers is",nsum)
print("Average of all the numbers is",navg)
print("There are",ecount,"even numbers")
print("Sum of even numbers is",esum)
print("Average of all even numbers is",eavg)
print("There are",ocount,"odd numbers")
print("Sum of odd numbers is",osum)
print("Average of all odd numbers is",oavg)
