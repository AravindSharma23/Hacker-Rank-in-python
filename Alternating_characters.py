"""
Alternating characters

"""
def alternatingCharacters(s):
    # Write your code here
    temp=""
    count=0
    for i in range(len(s)-2):
        temp=s[i+1]
        if s[i] == temp :
            count+=1
    if s[-1] == s[len(s)-2]:
        count+=1
    return count
