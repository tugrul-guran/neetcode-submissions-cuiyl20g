class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        opens = {'(', '{', '['}
        complete = {"()", "{}", "[]"}
        for bracket in s:
            if bracket in opens:
                stack.append(bracket)
            elif not stack:
                return False
            else:

                last = stack.pop()

                together = last + bracket

                if together not in complete:
                    return False

        if stack:
            return False

        return True