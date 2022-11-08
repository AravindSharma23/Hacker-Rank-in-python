"""
TO CHECK THE STRING IS Balanced or not 

"""

#
string = input()
bracket1 = ["{","(","["]
bracket2 = ["}",")","]"]
c1=0
c2=0
for s in string:
    if s in bracket1:
        c1+=1
    elif s in bracket2:
        c2+=1
if c1%2 == 0 and c2%2 == 0:
   print("Balanced")
else:
     print("NOt Balanced")

        

