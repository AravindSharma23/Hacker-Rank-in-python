"""
Sales by match-- Hacker rank

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
Sample Output

3  <---pairs of  duplicates number 


"""
arr=[1,1,3,1,2,1,3,3,3,3]
pair = 0
ar2 = []
for num in arr:
    if num in ar2 : 
        ar2.remove(num)
        pair +=1
    else: 
        ar2.append(num)
print(ar2)
