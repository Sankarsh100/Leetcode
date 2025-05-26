class Solution:
    def isValid(self, s: str) -> bool:
        # Mapping of closing to opening brackets
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for ch in s:
            if ch in pair:
                # Pop the top if available, else use a dummy
                top = stack.pop() if stack else '#'
                # If it doesn’t match the corresponding opening, invalid
                if pair[ch] != top:
                    return False
            else:
                # It’s an opening bracket—push onto the stack
                stack.append(ch)
        
        # If anything’s left, there was no matching closing bracket
        return not stack
