# Code likho jo check kare ki kya list palindrome hai ya nahi. 
# Aur print karo “Haan! palindrome hai” agar hai. Aur “nahi! Palindrome nahi hai” agar nahi hai.

#Abhi ke liye iss list ko use kar ke code likh sakte ho:

# name=[ 'n', 'i', 't', 'i', 'n' ]
# rev=name[::-1]
# if rev==name:
#     print("It's a palidrome")
# else:
#     print("It isn't a palidrome ")


# Apni list ko change kar ke alag alag values ke saath test out karo aur fir finally theek code ko upload karo.
# Inn values ke liye aap test kar sakte hai
# nayan => true naina => false anamana => true ainaania => true ainabnia => false

#using slicing #with user input:
name=list(input("Enter a word\n"))
rev=name[::-1]
if rev==name:
    print("It's a palidrome")
else:
    print("It isn't a palidrome")



#without using slicing
original=list(input("Enter a word:\n"))
reverse=[]
index=len(original)-1
while index >= 0 :
    reverse.append((original[index]))
    index=index-1
if original == reverse :
    print("It is a palidrome")
else:
    print("It isn't a palidrome")


string=list(input("Enter a word:\n"))
for i in range (len(string)):
    for k in range(i+1):
        if k == 0 :
            print((string[i]).upper(),end="")
        else:
            print(string[i],end="")
    print("_",end="")