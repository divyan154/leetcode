class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        vec = []
        ans = []
        for i in range(len(s)):
            if s[i] == '|':
                vec.append(i)
        
        for q in queries:
            l = bisect.bisect_left(vec, q[0]) # lower bound
            r = bisect.bisect_right(vec, q[1]) - 1
            
            val =  vec[r] - vec[l] - r + l if l < r else 0
            ans.append(val)
        return ans    
            