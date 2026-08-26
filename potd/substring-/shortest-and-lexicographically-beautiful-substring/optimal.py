class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        mini = float('inf')
        for i in range(n):
            temp = ""
            oneCount = 0
            for j in range(i , n):
                temp += s[j]
                if s[j] == '1':
                    oneCount += 1
                if oneCount == k :
                    mini = min(mini,len(temp)) 
                elif oneCount > k:
                    break       
        if mini == float('inf'):
            return ""         
        res = []
        for i in range(n):
            temp = ""
            oneCount = 0
            for j in range(i, n):
                temp += s[j]
                if s[j] == '1':
                    oneCount += 1
                if oneCount == k and len(temp) == mini:
                    res.append(temp)  
                elif oneCount > k:
                    break      

        return min(res)

    # TIme complexity - 0(N^3)
    # Space COmplexity - 0(N)
    # Notes - No need to take additional array , take another variable compare on the fly