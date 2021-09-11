#Ek code likho jo kisi bhi list ke liye yeh output karta hai, 
#ki uss list mei kitne odd numbers hai aur kitne even numbers hai.
elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
counter=0
counter1=0
i=1
while i<=len(str(elements)):
    for i in elements:
        if i % 2 == 0:
            counter=counter+1
        else:
            counter1=counter+1
    i=i+1
    print("There are",counter,"even numbers and",counter1,"odd numbers")
    