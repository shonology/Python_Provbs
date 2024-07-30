class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
          #reason for k=k%n is that if k is larger than list or array size it has to be made sure that it can shifted in corrected position that's why we use modulus operation
        n = len(nums)
        k = k % n 
        #this below technique is called slicing in python for shifting elements in right side 
        #for left we use this equation : nums[:]=nums[k:]+nums[:k]
        nums[:] = nums[-k:] + nums[:-k]  