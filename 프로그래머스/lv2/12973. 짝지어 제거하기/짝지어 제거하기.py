def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        
        elif stack[-1] == char:
            stack.pop()
        
        else:
            stack.append(char)
            
    return int(not stack)
        
            