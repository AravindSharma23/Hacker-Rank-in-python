"""
Super reduced string

"""
s="aaabccddd"
stack=[]
for char in s:
    if stack and char  == stack[-1]:
        stack.pop()
    else:
        stack.append(char)
print("".join(stack))
