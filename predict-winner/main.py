class Solution:
    def maxDiff(self,i : int, j : int , nums: List[int], dp:List[List[int]]) -> int:
        if i == j :
            return nums[i]
        if dp[i][j] != -1:
            return dp[i][j]    
        ans = max(nums[i] - self.maxDiff(i+1, j,nums,dp), nums[j] - self.maxDiff(i,j-1,nums,dp))
        dp[i][j] = ans
        return ans
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        if n % 2 == 0:
            return True
        dp = [[-1 for _ in range(n)] for _ in range(n)]  
           # Max Diff of both player's scores if they play optimally

        return True if self.maxDiff(0,n-1,nums,dp) >= 0 else False