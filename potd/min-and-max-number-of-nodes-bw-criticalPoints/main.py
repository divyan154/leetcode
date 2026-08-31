# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp = head
        prev = None
        pos = -1
        arr = []
        while temp != None:
            pos += 1
            if temp.next != None and prev != None:
                if temp.val > max(temp.next.val, prev.val) or temp.val < min(temp.next.val, prev.val):
                    arr.append(pos)
                    
            prev = temp
            temp = temp.next
        if len(arr) <= 1:
            return [-1,-1]
        if len(arr) == 2:
            return [arr[1] - arr[0],arr[1] - arr[0]]   
        n = len(arr)
        print(arr)
        maxi =  arr[n-1] - arr[0]
        mini = maxi

        for i in range(n-1):
            mini = min(mini, arr[i+1] - arr[i])
        return [mini, maxi]    



