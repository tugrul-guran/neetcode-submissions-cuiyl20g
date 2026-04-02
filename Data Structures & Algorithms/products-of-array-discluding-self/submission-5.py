class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []

        for i, _ in enumerate(nums):
            product = 1
            for j, num2 in enumerate(nums):
                if i != j:
                    product *= num2

            result.append(product)

        return result