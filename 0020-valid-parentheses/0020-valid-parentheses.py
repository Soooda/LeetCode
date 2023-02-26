class Solution:
    def isValid(self, s: str) -> bool:
        left = []
        
        for char in s:
            if char == "(" or char == "[" or char == "{":
                left.append(char)
            elif char == ")":
                if len(left) == 0:
                    return False
                elif left[-1] == "(":
                    del left[-1]
                else:
                    return False
            elif char == "]":
                if len(left) == 0:
                    return False
                elif left[-1] == "[":
                    del left[-1]
                else:
                    return False
            elif char == "}":
                if len(left) == 0:
                    return False
                elif left[-1] == "{":
                    del left[-1]
                else:
                    return False
            else:
                return True
        
        if len(left) == 0:
            return True
        return False