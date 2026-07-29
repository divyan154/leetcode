class Solution:
    def isPossible(self, weights: List[int], capacity, days: int) -> int:
        days_needed = 1
        n = len(weights)
        wt = 0
        for i in range(n):
            wt += weights[i]

            if wt > capacity:
                days_needed += 1
                wt = weights[i]
        print(f"Days Needded for capacity : {capacity} is {days_needed}")        
        return days_needed <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo = max(weights)
        hi = sum(weights)

        # ans = 

        while lo <= hi:
            mid = (lo + hi)//2
            if self.isPossible(weights, mid, days):
                hi = mid - 1
            else:
                lo = mid + 1   
        return lo


        