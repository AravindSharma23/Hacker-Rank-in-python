"""

Strong Password
"""



def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    nums = "0123456789"
    lwr = "abcdefghijklmnopqrstuvwxyz"
    upr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    spe = "!@#$%^&*()-+"

    count=0
    if any(a.islower() for a in password) == False :
        count+=1
    if any(a.isupper() for a in password) == False :
        count+=1
    if any(a.isnumeric() for a in password) == False :
        count+=1
    if any(a in spe for a in password)== False :
        count+=1
    return max(count,6-n)
        
