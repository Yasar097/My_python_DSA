class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opentoClose = {"}":"{" , "]":"[" , ")":"("}

        for c in s:
            if c in opentoClose:
                if stack and stack[-1] == opentoClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
