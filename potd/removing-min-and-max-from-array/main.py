class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        mini = float(inf)
        maxi = float(-inf)
        first_idx , second_idx = 0, 0
        for i in range(n):
            if nums[i] > maxi:
                maxi = nums[i]
                first_idx = i
            if nums[i] < mini:
                mini = nums[i]
                second_idx = i

        if first_idx > second_idx:
            first_idx , second_idx = second_idx, first_idx

        return min(second_idx + 1, min(n - first_idx, n - second_idx + first_idx + 1))  


 