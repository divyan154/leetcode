   def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        sz = len(strs)
        self.a = []
        dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(sz+1)]

        for s in strs:
            zeroes , ones = 0, 0
            zeroes = s.count('0')
            ones = s.count('1')
   
            self.a.append((zeroes,ones))


        for ind in range(sz-1,-1,-1):
            for nzeros in range(m+1):
                for nones in range(n+1):

                            if self.a[ind][0] > nzeros or self.a[ind][1] > nones: # i made a mistake here
                                dp[ind][nzeros][nones] = dp[ind+1][nzeros][nones]
                                continue               #also here
                                

                            # Take current string
                            take = 1 + dp[ind + 1][nzeros - self.a[ind][0]][nones - self.a[ind][1]]
                            # dont take current string
                            ntake = dp[ind + 1][nzeros][nones]
                            dp[ind][nzeros][nones] = max(take, ntake)