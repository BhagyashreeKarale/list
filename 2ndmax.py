#Code likho jo iss list mein se second maximum element (doosra sabse bada element) dhund kar kar print kare.
numbers= [50, 40, 23, 70, 56, 12, 5, 10, 7]
max = 0
for i in numbers:
  if max<i:
    max = i
secondmax = 0
for i in numbers:
  if secondmax<i:
    if i!=max:
      secondmax=i
print("Second largest number is:",secondmax)
########################################################################################################
#with user inputed list
numbers=int(input("Enter number of values"))
max=0
list1=[]
for i in range(numbers):
  ui=int(input("Enter a value:\n"))
  u2=ui
  list1.append(ui)
  if ui>max:
    max=ui
secondmax=0
for i in (list1):
  if int(i)>secondmax:
    if int(i)!=max:
      secondmax=i
print(max,"is the largest among the entered values")#position of print matters
# print(secondmax,"is the second largest among the entered values")




    
    






























