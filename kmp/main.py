class Solution:
    def computeLPS(self,pattern : str) :
        n = len(pattern)
        self.lps = [0] * n
        # prev Len of longest pref and sufix
        length = 0

        i = 1

        while i < n:

            if pattern[i] == pattern[length]:
                length += 1
                self.lps[i] = length
                i += 1
            elif length != 0:
                length = self.lps[length-1]
            else:
                self.lps[i] = self.lps[0]
                i += 1 
        

    def KMP(self, text : str, pattern : str) -> List[int]:
        i , j = 0 , 0
        m = len(text)
        res = []

        while i < m:
            if text[i] == pattern[j]:
                i +=1 
                j += 1
            if j == len(pattern):
                res.append(i-j)
                j = self.lps[j-1]     
            if i < m and text[i] != pattern[j]:
                if j != 0:
                    j = self.lps[j-1]
                else :
                    i += 1
        return res                                   


    def strStr(self, haystack: str, needle: str) -> int:
        self.computeLPS(needle)
        result = self.KMP(haystack,needle)
        ans = -1 if len(result) == 0 else result[0]
        return ans
 


        # Notes 

        # 1 - Time complexity - O(M+N) -- KMP SOlution , Naive Solution - O (M*N)
        # 2 - Lps array tells the len of longest proper prefix that is also suffix

