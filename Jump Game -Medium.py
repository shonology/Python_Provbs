class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # Initialize the maximum reachable index
        n = len(nums)

        for i in range(n):
            if i > max_reachable:  # If current index is greater than the maximum reachable index, return False
                return False
            max_reachable = max(max_reachable, i + nums[i])  # Update the maximum reachable index
            if max_reachable >= n - 1:  
                # If the maximum reachable index is greater than or equal to the last index, return True
                return True

        return max_reachable >= n - 1  # check if we can reach the last index