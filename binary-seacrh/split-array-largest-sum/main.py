class Solution:
    def isPossible(self, cap: int, nums:List[int] , k : int) -> bool:
        cuts = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > cap:
                cuts += 1
                cur_sum = nums[i]


        return cuts + 1 <= k        


    def splitArray(self, nums: List[int], k: int) -> int:
        lo = max(nums)
        hi = sum(nums)
        # if len(nums) < k:
        #     return 
        while lo <= hi:
            mid = (lo + hi)//2
            if self.isPossible(mid, nums, k):
                hi = mid - 1
            else:
                lo = mid + 1    
        return lo
