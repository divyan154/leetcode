class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ind = bisect_left(nums, True, key = lambda n: n <= nums[-1])
        lo , hi = ind , ind + n - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi)//2
            if nums[mid%n] == target:
                ans = mid % n
                return ans 
            elif nums[mid%n] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return  ans                
        

        