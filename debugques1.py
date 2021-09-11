#wrong code
marks = ["10", "32", "42", "65", "67", "89", "76", "38", "67"]
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + marks[counter]
    counter = counter + 1
#correct code
marks = [10, 32, 42, 65, 67, 89, 76, 38, 67]#string coverted to integers as we want the sum of the intergers.
total_marks = 0
counter = 0
while counter < len(marks):
    total_marks = total_marks + marks[counter]
    counter = counter + 1
print(total_marks)#print was missing because of which we weren't able to see the output

