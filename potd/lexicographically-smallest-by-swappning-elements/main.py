class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted  = sorted(nums)

        curr_group = 0
        num_to_group = {}
        group_to_list = {}
        group_to_list[curr_group] = deque([nums_sorted[0]])

        num_to_group[nums_sorted[0]] = curr_group

        for i in range(1, len(nums_sorted)):
            # new group
            if abs(nums_sorted[i] - nums_sorted[i - 1]) > limit:
                curr_group += 1
            num_to_group[nums_sorted[i]] = curr_group

            # Add element to sorted group deque
            if curr_group not in group_to_list:
                group_to_list[curr_group] = deque()
            group_to_list[curr_group].append(nums_sorted[i])

        # Iterate through nums and overrite each element with next element in its corresponding group
        for i in range(len(nums)):
            num = nums[i]
            group = num_to_group[num]
            nums[i] = group_to_list[group].popleft()
        return nums    




        