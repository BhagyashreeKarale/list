# Is Magic Square?
# Magic Square woh square hota hai jismei - har row ka, har column ka, and dono diagonals ka sum same hota hai.

# Aapko yeh program likhna hai - jo ek nested list leta hai, aur dekhta hai ki woh magic square hai ya nahi?

# E.g. Yeh magic square hai, kyuki

magic_square = [[8, 3, 4],
                [1, 5, 9],
                [6, 7, 2]]
ssum=0
for i in range (len(magic_square)):
    for j in range (len(magic_square[i])):
        if i==j:
            ssum=ssum+magic_square[i][j]
psum=0
for i in range (len(magic_square)):
    for j in range (len(magic_square[i])):
        if i+j==len(magic_square[i])-1:
            psum=psum+magic_square[i][j]
for i in range (len(magic_square)):
    c1sum=0
    c2sum=0
    c3sum=0
    for i in range(len(magic_square)):
        for j in range (len(magic_square[i])):
            if j==0:
                c1sum=c1sum+magic_square[i][j]
            elif j==1:
                c2sum=c2sum+magic_square[i][j]
            elif j==2:
                c3sum=c3sum+magic_square[i][j]
r1sum=0
r2sum=0
r3sum=0
for i in range(len(magic_square)):
    for j in magic_square[i]:
        if i==0:
            r1sum=r1sum+j
        elif i==1:
            r2sum=r2sum+j
        elif i==2:
            r3sum=r3sum+j
if r1sum==r2sum==r3sum and c1sum==c2sum==c3sum and psum==ssum:
    print("It is a Magic Square")
else:
    print("It isn't a Magic Square")







































# sum=0
# for i in range(len(magic_square)):
#     sum=sum+magic_square[i][2-i]

