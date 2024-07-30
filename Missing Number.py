class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        summ = n * (n + 1) // 2 # sum of n natural numbers

        arr_sum = sum(nums) # sum of array numbers
        miss_sum= summ - arr_sum # subtract from total sum by array sum of values to get missing values
        return miss_sum
        