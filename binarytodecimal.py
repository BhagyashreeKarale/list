# Binary to Decimal
# Iss program mei humein agar koi number binary form mei diya gaya hai, 
# toh hum uski decimal form nikalna seekhenge.
# Jaise yeh diagram dekho.
binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
power=0
sum=0
rev=binary_number[::-1]#list should be reversed
for i in rev:
    sum=sum+(i*(2**power))
    power=power+1
print(sum)



# Iss number ko decimal form mei karne ke liye, hum

# # last element ko 2^0 yaani 1 se
# # second last element ko 2^1 yaani 2 se
# # third last element ko 2^2 yaani 4 se
# # fourth last element ko 2^3 yaani 8 se
# # ...
# # ...
# # 
# # multiply kar kar
# # add karna hai

# Aise karne se uppar wali list ka answer 155 aayega.

# Edge Case
# binary_number = [1, 0, 0, 2, 1]

# Aapka program iss case mei kya output deta hai? Aapke program agar robust hoga, toh bolega invalid output, nahi toh error throw karega.

# binary_number = [1, 0, 0, "1", 1]

# Aapka program iss case mei kya output deta hai? Aapke program agar robust hoga

# Par robust nahi hoga, toh error throw karega.
#############################################################################################################################
#converting decimal to binary
ui=int(input("Enter the number:\n"))
blist=[]
while ui>0:
    r=ui%2
    blist.append(r)
    ui=ui//2
rev=blist[::-1]
print("It's binary form is:")
for i in rev:
    print(i,end="",)


