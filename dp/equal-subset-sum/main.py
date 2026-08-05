class Solution:
    def sumPresent(self, ind, target, nums, dp) -> bool:
        # print(target)
        # base case
        if target == 0:
            return True
        if ind == len(nums):
             return False   
        if dp[ind][target] != None:
            # print()
            return dp[ind][target]
        # Take the value if value <= T
        take , ntake = False, False
        if nums[ind] <= target:
            if self.sumPresent(ind + 1, target - nums[ind], nums,dp):
                dp[ind][target] = True
                return dp[ind][target]
        ntake = self.sumPresent(ind +1 , target, nums, dp)

        if take or ntake:
            dp[ind][target] = True
            return True
        dp[ind][target] = False     
        return False 
                 
    def canPartition(self, nums: List[int]) -> bool:
        # sz = len()
        dp = [[None for _ in range(10001)] for _ in range(len(nums))]
        tSum = sum(nums)
        if tSum % 2 :
            return False
        

        return self.sumPresent(0, tSum//2, nums, dp)

        