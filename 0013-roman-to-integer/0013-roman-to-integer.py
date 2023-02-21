class Solution:
    def romanToInt(self, s: str) -> int:
        ret = 0
        i = 0
        
        while i < len(s):
            char = s[i]
            if char == 'M':
                ret += 1000
            elif char == 'D':
                ret += 500
            elif char == 'C':
                if i + 1 == len(s):
                    ret += 100
                elif s[i+1] == 'D':
                    ret += 400
                    i += 1
                elif s[i+1] == 'M':
                    ret += 900
                    i += 1
                else:
                    ret += 100
            elif char == 'L':
                ret += 50
            elif char == 'X':
                if i + 1 == len(s):
                    ret += 10
                elif s[i+1] == 'L':
                    ret += 40
                    i += 1
                elif s[i+1] == 'C':
                    ret += 90
                    i += 1
                else:
                    ret += 10
            elif char == 'V':
                ret += 5
            elif char == 'I':
                if i + 1 == len(s):
                    ret += 1
                elif s[i+1] == 'V':
                    ret += 4
                    i += 1
                elif s[i+1] == 'X':
                    ret += 9
                    i += 1
                else:
                    ret += 1
            
            i += 1
        return ret