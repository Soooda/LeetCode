def contain_duplicate(s):
    hashmap = {}
    for char in s:
        if char not in hashmap:
            hashmap[char] = 1
        else:
            return True
    return False

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        ret = 1
        
        for window_size in range(2, len(s) + 1):
            stop = True
            
            for i in range(len(s) - window_size + 1):
                window = s[i:i + window_size]
                if not contain_duplicate(window):
                    stop = False
                    break
            
            if stop:
                break
            else:
                ret = window_size
            
        return ret