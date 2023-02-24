# You are given an array nums of n positive integers.

# You can perform two types of operations on any element of the array any number of times:

# If the element is even, divide it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
# If the element is odd, multiply it by 2.
# For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
# The deviation of the array is the maximum difference between any two elements in the array.

# Return the minimum deviation the array can have after performing some number of operations.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            if num % 2 == 0:
                num = -num
            
            else:
                num = -num * 2

            heapq.heappush(max_heap, num)

        
        min_dev = float('inf')
        min_val = -max(max_heap)

        while len(nums) == len(max_heap):
            curr = -heapq.heappop(max_heap)
            min_dev = min(min_dev, curr- min_val)
            if curr % 2 == 0:
                min_val = min(min_val, curr//2)
                heapq.heappush(max_heap, -curr//2)
            else:
                break
        
        return min_dev