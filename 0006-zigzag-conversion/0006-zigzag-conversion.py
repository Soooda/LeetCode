class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Line = 2
        P Y A I H R N
        A P L S I I G
        Line = 3
        P   A   H   N
        A P L S I I G 
        Y   I   R
        Line = 4
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        '''
        if numRows == 1:
            return s

        ret = ""
        # Line 1
        ret += s[::numRows + (numRows - 2)]

        # Middle lines
        for n in range(1, numRows - 2 + 1):
            temp = ""
            for i in range(len(s)):
                # Vertical
                if i % (numRows + numRows - 2) == n:
                    temp += s[i]
                # Diagonal
                elif i % (numRows + numRows - 2) == numRows + numRows - 2 - n:
                    temp += s[i]
            ret += temp

        # Last Line
        ret += s[numRows - 1::numRows + (numRows - 2)]

        return ret