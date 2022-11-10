"""
Breaking the records

"""
def breakingRecords(scores):
    # Write your code here
    large=scores[0]
    small = scores[0]
    mini = 0
    maxi = 0
    
    for i in range(1,len(scores)):
        if large < scores[i]:
            large = scores[i]
            maxi+=1
        if small > scores[i]:
            small = scores[i]
            mini +=1
    a = maxi,mini
    return a
    
    
