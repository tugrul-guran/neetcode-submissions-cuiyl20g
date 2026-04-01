class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remainder_to_index = {}

        for index, num in enumerate(nums):

            if num in remainder_to_index:
                return [remainder_to_index[num], index]
            
            remainder = target - num
            remainder_to_index[remainder] = index