"""
Compare the Triplets


"""


a=[17,28,30]
b=[19,16,8]
c1=0
c2=0
res1=[]
res2=[]
for i in range(len(a)):
    if a[i]>b[i]:
        c1+=1
        
    if b[i]>a[i]:
        c2+=1
        
res1.append(c1)
res2.append(c2)
final=res1+res2
print(final)
