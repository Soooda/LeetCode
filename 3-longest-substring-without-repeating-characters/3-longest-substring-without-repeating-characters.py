class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        has = {}
        current_len = 0
        max_len = 0
        i,j = 0,0
        
        while j < len(s):
            
            while s[j] in has:
                has.pop(s[i])
                i += 1
                current_len -= 1
                
            if s[j] not in has:
                has[s[j]] = 1
                current_len +=1
                if max_len < current_len:
                    max_len = current_len
            j +=1
        
        return(max_len)