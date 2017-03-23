class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def lastPosition(self, A, target):
        # Write your code here
        if A == None or len(A) == 0:
            return -1
            
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) / 2
            
            if A[mid] < target:  
                start = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid
                
        if target == A[end]:
            return end
        elif target == A[start]:
            return start
        else:
            return -1
     
A = [1, 2, 2, 4, 5, 5]
s = Solution()
print(s.lastPosition(A, 5))  
