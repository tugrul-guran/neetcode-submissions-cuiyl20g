class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_indices = []
        right_indices = []
        result = []

        l = len(nums)

        current_product = 1
        for num in nums:
            left_indices.append(current_product)

            current_product *= num

        current_product = 1
        for index in range(l - 1, -1, -1):
            right_indices.append(current_product)

            current_product *= nums[index]

        current_product = 1
        for index in range(l):
            result.append(left_indices[index] * right_indices[l - 1 - index])

        return result
"""
1 2 4 6

at 0, I do: 2 * 4 * 6
at 1, I do: 1 * 4 * 6
at 2, I do: 1 * 2 * 6
at 3, I do: 1 * 2 * 4


index0 from the left: 1
index0 from the right: 48

index1 from the left: 1
index1 from the right: 24

index2 from the left: 2
index2 from the right: 6
"""
