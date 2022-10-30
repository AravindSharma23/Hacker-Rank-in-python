# Plus minus


def plusMinus(arr):
    # Write your code here
    c1=0
    c2=0
    c3=0
    res1=0
    res2=0
    res3=0
    for a in arr:
        if a > 0:
            c1+=1
            res1=c1/n
            
        if a < 0:
            c2+=1
            res2=c2/n
           
        if a == 0:
            c3+=1
            res3=c3/n
           
    print("{0:0.6f}".format(res1)) # +ve
    print("{0:0.6f}".format(res2)) # -ve
    print("{0:0.6f}".format(res3)) # 0
            
