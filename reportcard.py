#Iss list ko dekhein:

marks = [[78, 76, 94, 86, 88],
        [91, 71, 98, 65, 76],
        [95, 45, 78, 52, 49]]


# Yeh kisi student ke peechle teen saal ke marks hai. 
# Aap ko teeno saalo, ke sab subjects ke marks ka total calculate karna hai.

# Jaise uppar di hui nested list ka sum - 1142 aayega.

# Edge Cases:
# Check your program for following nested lists as well (bina code change kiye chalna chahiye, nahi toh aapne sahi se code nahi likha):

# marks =[[78, 76, 94, 86, 88],
#        [91, 71, 98, 65],
#        [95, 45, 78]]

# Jaise uppar di hui nested list ka sum - 965 aayega.

# marks = [78, 76, 94, 86, 88],
#         [91, 71, 98, 65],
#         [95, 45, 78],
#         [87, 67, 49, 68, 88]

# Jaise uppar di hui nested list ka sum - 1124 aayega.
marks = [[78, 76, 94, 86, 88],
        [91, 71, 98, 65, 76],
        [95, 45, 78, 52, 49]]
sum=0
sum1=0
i=0
for i in marks:
    for i in i:
        sum=sum+i
print(sum)