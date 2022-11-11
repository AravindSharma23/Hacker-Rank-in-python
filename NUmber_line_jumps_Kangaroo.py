"""
NUmber LIne JUmps -- Kangaroo

"""
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v2> v1 :
        return "NO"
    while x1<x2:
        x1 = x1+v1
        x2 = x2+v2
        if x1 == x2 :
            return "YES"
   return "NO

