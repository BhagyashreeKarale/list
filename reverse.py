#Code likho jo neeche di gayi lists ke items ko reverse order yaani ki ulta print kare.
places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
# Aapke code ka outut yeh hona chaiye:
# kerela
# punjab
# rajasthan
# gujrat
# delhi
# Hints
# Jab index i hai, tab length - i -1 index par kya hoga.

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]
places=[6,7,8,4,3,2,6]

# i	places[i]	  length - i	places[length - i]
# 0	"delhi"	        4	        "kerala"
# 1	"gujrat"	    3	        "punjab"
# 2	"rajasthan"	    2	        "rajasthan"
# 3	"punjab"	    1	        "gujrat"
# 4	"kerala"	    0	        "delhi"

# place=len(str(places))-i
for i in places:
    pass
print(places[::-1])#-1 starts from the end/right hence it can be used to reverse any list