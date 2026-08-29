class Solution:
    def subarrayXor(self, arr, m):
        countOfPreviousXors = {}
        countOfPreviousXors[0] = 1
    
        cnt = 0
        xor = 0
    
        for i in range(len(arr)):
            xor = xor ^ arr[i]
    
            target = xor ^ m
    
            if target in countOfPreviousXors:
                cnt += countOfPreviousXors[target]
    
            countOfPreviousXors[xor] = countOfPreviousXors.get(xor, 0) + 1
    
        return cnt