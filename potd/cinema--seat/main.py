class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Exact binary representations of the favorable case
        left, middle, right,  = 0b11110000 , 0b11000011, 0b00001111
        occupied = collections.defaultdict(int)

        for seat in reservedSeats:
            if 2 <= seat[1] <= 9:
                occupied[seat[0]] |= 1 << (seat[1] - 2)

        ans = 2 * (n - len(occupied))   

        for row , bitmask in occupied.items():
            if ((bitmask | left == left)
            or (bitmask | middle == middle)
            or (bitmask | right == right)) :
               ans += 1
        return ans       










        