class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  #hash map method where we store index of the number 
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []  #return empty if no target value found