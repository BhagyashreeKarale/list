# 50 50 Lifeline
# 50 50 Lifeline
# Ab aapko 50 50 lifeline implement karni hai, user answer karte time, 
# answer mei 1,2,3 ya 4 ke alaway ab 5050 bhi daal sakta hai. 
# Agar user 5050 daalega, toh aapko user ko

# sirf uss question ke liye
# dobara se do options dikhane hai
# dobara se user input lena hai
# aur phir jaisa aap pehle kar rahe the, wohi code chalna chahiye, yaani
# sahi answer to - batayie - right answer hai
# galat answer to - tell user - wrong answer hai

# Dhyaan Rakhein
# Jo do options aap denge - unemi se ek answer theek hi hona chahiye
# Bonus Task
# Apne code ko aise likhiye, ki user sirf ek baar 5050 lifeline use kar sakta hai. 
# User agar doosri baar try karta hai, toh usse boliye, ki aap already lifeline use kar chuke hai.

question_list = ["How many continents are there?",              # pehla question
                 "What is the capital of India?",               # doosra question
                 "NG mei kaun se course padhaya jaata hai?"]    # teesra question

options_list = [["1.Four", "2.Nine", "3.Seven", "4.Eight"],                              #pehle question ke liye options
                ["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],                    #second question ke liye options
                ["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]#third question ke liye options

lifeline_list=[["3.Seven", "4.Eight"],                              #pehle question ke liye options
                ["2.Bhopal", "4.Delhi"],                    #second question ke liye options
                ["1.Software Engineering","4.Agriculture"]]#third question ke liye options

life_count=0
solution_list = [3, 4, 1]
for i in range(len(question_list)):
    print(question_list[i])
    for j in options_list[i]:
        print(j)
    oinput=input("Do you want to use 50-50 lifeline?(yes/no)\n")
    if oinput=="yes":
        life_count=life_count+1
        if life_count<=1:
            for f in lifeline_list[i]:
                print(f) 
            ainput=int(input("\nEnter the correct option number:\n"))
            if solution_list[i] == ainput:
                print("Congratulations!Correct answer.\n")
            else:
                print("Better luck next time:)")
                break
        else:
            print("You have already used 50-50 lifeline\nStart again!")
            break
    else:
        ainput=int(input("\nEnter the correct option number:\n"))
        if solution_list[i] == ainput:
            print("Congratulations!Correct answer.\n")
        else:
            print("Better luck next time:)")
            break