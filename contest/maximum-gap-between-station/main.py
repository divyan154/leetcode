class Solution:
    def maximumGap(self, skill: str, station: str) -> int:
        n = len(skill)
        m = len(station)
        leftMostPosition = [0] * n
        rightMostPostion = [0] * n
        
        j = 0
        for i in range(n):
            print(i)
            while skill[i] != station[j] :
                j += 1
            leftMostPosition[i] = j
            j += 1   

        #  Right Most Position
        j = m - 1
        for i in range(n - 1, -1, -1):
            while skill[i] != station[j]:
                j -= 1
            rightMostPostion[i] = j
            j -= 1
        
        ans = 0
        for i in range(n - 1): 
            ans = max(ans, rightMostPostion[i + 1] - leftMostPosition[i])
        return ans    


  #
  # Time Complexity
  # O(N + M ) 
  # In First Look, It looks like O(N*M) but j donesnt reset. it keeps moving  

