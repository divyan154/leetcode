class Solution:
    def reverseString(self, s: str) -> str:
        n = len(s)
        s = list(s)
        i , j = 0 , n - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)    

# TIme complexity - 0(N)
# Space complexity - 0(1)
        