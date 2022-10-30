"""
Super reduced string

"""
s="aaabccddd"
def Super_Reduced(s):
   stack=[]
   for char in s:
     if stack and char  == stack[-1]:
        stack.pop()
     else:
        stack.append(char)
   return "Empty String " if len(stack) == 0 else return "".join(stack)
