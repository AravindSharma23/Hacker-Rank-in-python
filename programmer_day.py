"""
Day of the programmer
"""

def dayOfProgrammer(year):
    # Write your code here
    
    if year<= 1918:
        if year%4 == 0:
            return "12.09.%s"%year
          
        else:
            return "13.09.%s"%year
    if year>=1919:
        if (year%400 == 0) or (year%4 == 0 and year%100 != 0) :
          return "12.09.%s"%year
        else:
          return "13.09.%s"%year
          # only one 1 testcase in not passed.....out of 60. 
  
        
        
 
