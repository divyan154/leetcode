class Solution:
    def isPossible(self, quantities: List[int], maxi: int ,n: int) -> int:
        sz = len(quantities)
        stor_need = 0
        for i in range(sz):
            stor_need += math.ceil(quantities[i]/maxi)

        return stor_need <= n   

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        lo = 1 
        hi = max(quantities)

        while lo <= hi:
            mid = (lo + hi)//2
            if self.isPossible(quantities, mid, n):
                hi = mid - 1
            else:
                lo = mid + 1  
        return lo    