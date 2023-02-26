class Solution:
    def overlap(self, s1, s2):
        ret = ""
        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                ret += s1[i]
            else:
                break
        return ret
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        ret = strs[0]
        for s in strs:
            ret = self.overlap(ret, s)
        
        return ret