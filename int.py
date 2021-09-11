element_list = []
list_len = int (input ( "Enter the length of your list:\n" ) )
for i in range (list_len):
    element=input("Enter element "+str(i+1)+":\n")
    element_list.append(element)
limit=int(input("Enter index number of the element from which you want to reverse:\n"))
k=limit
r=-1
while k<=list_len:
    element_list[k]=element_list[r]
    k=k+1
    r+=-1
print(element_list)
