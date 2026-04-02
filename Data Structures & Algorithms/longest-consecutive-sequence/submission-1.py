class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values_set = set(nums)

        seq_vals = []
        result = 0
        for num in nums:
            if num - 1 not in values_set:
                current_length = 0
                mover = 0
                while num + mover in values_set:
                    current_length += 1
                    mover += 1
                result = max(result, current_length)

        return result