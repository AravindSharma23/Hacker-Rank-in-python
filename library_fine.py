"""
Library Fine
"""
def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine=0
      
    if d2<d1 and m2==m1 and y2 == y1: # days exceeded
      fine=15*(d1-d2)
    elif m2<m1 and y2 == y1: # month exceeded
      fine=500*(m1-m2)
    elif y2 < y1: # year exceeded
        fine=10000
    return fine


