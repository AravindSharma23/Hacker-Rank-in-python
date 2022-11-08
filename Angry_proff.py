"""
Angry Professor
"""
def angryProfessor(k, a):
    # Write your code here
    count=0
    for i in range(len(a)):
        temp=a[i]
        if int(temp)<=0:
            count+=1
    if count >= k:
        return "NO"
    else:
        return "YES"

