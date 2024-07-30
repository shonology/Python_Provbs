class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZeroFoundAt = 0
        #this loop would get all non zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        #this loop would give the list/array with remaining 0
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0
