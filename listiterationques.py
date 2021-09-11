#Code likho jo di gayi list mein jo number 20 se bade hai aur 40 se chote hai unhe count kare. 
# Aur firr unka count print kare.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7,30,28]
count=0
for i in numbers:
    if i>20 and i<40:
        count=count+1
print("There are",count,"numbers greater than 20 and smaller than 40 present in the list")