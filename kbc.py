# Kaun Banega Codepati (KBC) - Setup
# Lists ke baare mein seekhne ke liye 
# hum Kaun Banega Crorepati jaise ek game banayenge python ka use kar ke.
# Yeh code dekh kar samjhe - ki kaise humne KBC game banane ke liye, 
# kuch important cheezein define ki hai - jaise - questions, options aur unke solutions.

question_list = ["How many continents are there?",              # pehla question
                 "What is the capital of India?",               # doosra question
                 "NG mei kaun se course padhaya jaata hai?"]    # teesra question

options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],                              #pehle question ke liye options
                ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],                    #second question ke liye options
                ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]#third question ke liye options

solution_list = [3, 4, 1]
for i in range(len(question_list)):
    print(question_list[i])
    for j in options_list[i]:
        print((j))
    ainput=int(input("\nEnter the correct option number:\n"))
    if solution_list[i] == ainput:
        print("Congratulations!Correct answer.\n")
    else:
        print("Better luck next time:)")
        break


# har ek question ke liye, uski solution key (yeh index nahi hai)
# solution_list = [3, 4, 1]
# for i in range(len(question_list)):
#     for i in question_list:
#         q1input=input("Yeh aapka question:\n",print(i))
############################################################################################
# Part 1
# Humein unn lists ko use kar kar, yeh information print karni hai:

# question_list variable ko use kar kar doosra question print karo 
# options_list ka use kar kar doosre question ke chaaron options ko print karo

# Aapka output kuch aisa aana chahiye:

# Aapka Sawaal hai:
# What is the capital of India?

# Aapke options hai:
# 1. Chandigarh
# 2. Bhopal
# 3. Chennai
# 4. Delhi

# Dhyaan Rakhein
# Har option ke saath uska number bhi print karna hai

# Hint:
# Yaad karo aapne indexes ke baare mein kya pada tha
# Options ko print karne ke liye loop use karo
