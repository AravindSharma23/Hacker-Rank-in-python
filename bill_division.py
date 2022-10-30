"""
BILL DIVISION
bill  <-- food ordered array
k <-- anna neglected item to eat
b <-- 
"""
def bonAppetit(bill, k, b):
    # Write your code here
    tot=0
    for i in bill:
        tot+=i
    billing=(tot-bill[k])//2
    charged=b-billing
    if billing < b:
        print(charged)
    else:
        print("Bon Appetit")
