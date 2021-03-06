################################################### lists-operations ######################################################
# Lists ke saath kya kar sakte hain?
# Iss exercise mei hum samjhenge ki LISTS ko kaise use karte hai. Jaisa humne dekha LIST mei kaafi values hoti hai. Toh hume koi tareeka chahiye jisse hum in values ko access kar paye.

names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print (names_list[1])

# [1] likhne karne se kya hua? "shivam" print hua?

# Yaha par 1 ko INDEX bolte hai. Kisi item ko access karne ke liye uska INDEX daalte hai. 
# Dekhte hai iss list mei sabka INDEX kya hai.
# ["annu", "shivam", "deepa", "pooja", "rupa"]
# annu ka index 0
# shivam ka index 1
# deepa ka index 2
# pooja ka index 3
# rupa ka index 4

# Agar aap dhyaan se dekhenge toh aap samjhenge ki INDEX uss ITEM ki position se 1 kam hota hai, 
# kyunki index ki ginti 0 se shuru hoti hai aur 1 se nahi.
# ["annu",	"shivam",	"deepa",	"pooja",	"rupa"]
#    0	        1	        2	       3	       4

names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print (names_list[0]) # se "annu" print hoga
print (names_list[4]) # se "rupa" print hoga
print (names_list[5])

# Kya last line se error aati hai? Error aayi -
# list index out of range
# Iska matlab simple - jo INDEX aapne diya hai woh List ke indices (indices - index ka plural hai) ki range se baahar hai
#######################################################################################################################
# Question
# maximum INDEX hum kitna daal sakte hai?

# Answer
# INDEX ki length se ek kam. Usse zyada daalne se index out of range error aayegi.
# Error ke baare mein google kar ke thoda aur samjho. 
# Yeh error aapka peecha nahi chodegi ;) Behetar hai, abhi thoda samajh jayein!
########################################################################################################################
# Changing List Items
# Issi tarah se hum LIST mei ITEMS ko update/change bhi kar sakte hai.
names_list[0] = "abhishek"
print (names_list)
# Kya dekha aapne? Jo 0 INDEX par ITEM tha woh change ho kar "abhishek" ho gaya. Issi tarah se yeh code run karo.

names_list[3]="rishabh"
print (names_list)

# Jo 3 INDEX par ITEM tha woh change ho kar "rishabh" ho gaya. 
# Dhyaan rakhe, ki INDEX item ki position se ek kam hota hai. Aise hi agar aap yeh likhoge:
names_list[5]="dhruv"
# Aapko list index out of range error milegi, kyuki 5th index par koi ITEM exist nahi karti
# Length of List and Adding values of the List

# Agar humne apne code mein ek list ki length dekhni hai, toh hum len function ka use kar sakte hain.
names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
print (len(names_list))
#########################################################################################################################3
# Agar humne list mein ek nayi value daalni hai toh hum append function use kar ke daal sakte hain. 
# append function ka use kar ke hum list ke aakhir mein ek nayi value daal sakte hain.
print (names_list)
names_list.append("dhruv")
print ("length of the list is ", len(names_list))
print (names_list)

# Yahan dekho ki append function se pehle list ki length 5 thi aur uske baad 6 ho gayi. 
# Jab appne names_list print kari toh dekho ki dhruv ki value last mein add ho gayi.

# Ek aur baar append kar ke dekhte hain.

names_list.append("alok")
print ("length of the list is ", len(names_list))
print (names_list)

# Issi tarah se aap kitne bhi elements add kar sakte hai
######################################################################################################################
# Removing Elements from a List
# Jaise hum list se elements add kar rahe the, waise hi elements remove bhi kar sakte hain.

# List se agar aakhiri element hatana ho toh uske liye pop function use karte hai.

names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
names_list.pop()
print ("length of the list is ", len(names_list))
print (names_list)

# Print karke dekho ki aakhri element hatt gaya hoga. Firse ek aur element remove kar ke dekhte hain.

names_list.pop()
print ("length of the list is ", len(names_list))
print (names_list)

# Aap list par pop function kisi argument ke saath bhi call kar sakte hai. Yaani aap pop mei kuch index daal sakte hai, jaisa karne par, uss list se, uss index ka element remove ho jayega.

# Example:

print ("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print ("length of the list is ", len(names_list), names_list)
names_list.pop(2)
print ("length of the list is ", len(names_list), names_list)
###############################################################################################################
# Check if Element exists in List
# List mei kaafi saari interesting operations kiye ja sakte hai. 
# Unmei se ek operation hai yeh dekhna ki koi particular ITEM LIST mei belong karta hai ya nahi. Jaise:
"shivam" in names_list
# Iska result True aayega kyunki "shivam" names_list mein exist karta hai."imtiyaz" in names_list

# Iska result false aayega kyunki "imtiyaz" names_list mein exist nahi karta.
# Kyunki yeh ek boolean value (True/False) return karta hai, hum isko If statement ke saath use kar sakte hain. Jaise:

if "shivam" in names_list:
    print ("Shivam ka naam names_list mei hai")
else:
    print ("Shivam ka naam names_list mei nahi hai.")
#Yaad kariye humne booleans ke baare mein last lessons mein kya pada tha.