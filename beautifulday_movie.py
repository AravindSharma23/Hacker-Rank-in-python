"""
Beautiful daY AT THE MOVIE

"""
def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for i in range(i,j+1):
        num=str(i)
        rev=num[::-1]
        days=abs(i-int(rev))/k
        if days == int(days):
            count+=1
    return count
            

